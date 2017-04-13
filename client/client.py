import logging
import docker
from docker.errors import ContainerError
import json

# Enable logging (console)
logger = logging.getLogger('app')
logger.setLevel(logging.ERROR)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)


CREDS = {"APIC_URL": "http://10.94.140.72",
         "APIC_LOGIN": "admin",
         "APIC_PASSWORD": "ins3965!"
        }

class Job(object):
    """
    A base job
    """

    def __init__(self, id=None, json=None, text=None):
        self.json = json
        self.text = text
        self.id = id


    def execute(self):
        # Job Dispatcher, identifies type and calls the appropriate handler

        # if this is a docker job
        if self.json and 'DockerJob' in self.json:
            result = DockerJob(image=self.json['DockerJob']['image'])
            return result.execute()
        else:
            return "foo"


class DockerJob(Job):
    """
    a docker based plugin job
    """
    def __init__(self, image=None):
        """
        Docker Jobs are initialized using a simple image name which is accessible
        :param image: str dockerhub image e.g collins-plugins/docker
        :return:
        """
        self.image = image


    def execute(self):

        # now we just fire an instance containter image, docker magic ensues
        # returns a response of some sort

        # Check for container runtime errors first
        try:
            logging.debug("Attempting to launch container from image {}".format(self.image))
            container_output = client.containers.run(self.image, environment=CREDS)
            logging.debug("container output={} ".format(container_output))

        except docker.errors.ContainerError as e:
            # The container raised an error when ran
            return Failure(e)
        except docker.errors.ImageNotFound as e:
            # The plugin was not found
            return ImageNotFoundResponse(e)

        # Engine Successfully ran the container,
        try:
            # we get a json response back from container
            json_from_container = json.loads(container_output)
            return Result.from_response(json_from_container)

        except ValueError:
            # if the plugin does not provide valid JSON, this job has failed
            return Failure(container_output)

        # should never get here
        ret = {"result": "unknown"}

        return ret


class Result(object):

    """
    Results Dispatcher

    """
    @classmethod
    def from_response(cls, enginemsg):

    #def __init__(self, enginemsg):
        try:
            logger.debug("Checking for JSON response from engine response: {}".format(enginemsg))
            if isinstance(enginemsg, str):
                logger.debug("Attempting to load json data")
                jsondata = json.loads(enginemsg)
            elif isinstance(enginemsg, dict):
                logger.debug("Creating result from dictionary: {}".format(enginemsg))
                jsondata = enginemsg
                # the plugin returned proper json, so it should give us a result

            if jsondata['result'] == 'Passed':
                logger.debug("Job Marked successfull")
                return Success(enginemsg)
            elif 'result' in jsondata and jsondata['result'] == 'Failed':
                logger.debug("Job Marked failed")
                return Failure(enginemsg)

        # if we don't get json back the testfailed
        except ValueError:
            return Failure(enginemsg)

        except TypeError as e:
            logger.debug("TYPEERROR {}:".format(e))
            return Failure(enginemsg)




    pass

class Success(Result):
    """
    base success object provides a json response child classes may implement more sophisticated response
    """
    def __init__(self, enginemsg):
        """

        :param enginemsg: container output from exitcode 0
        :return:
        """
        self._msg = enginemsg
        self._json = None
        self._html = None
        self.text = "Passed"

        # Result Should have valid json, we load it up here
        try:
            self.as_dict = json.loads(enginemsg)
            self._json = enginemsg
        # Except when it doesn't
        except ValueError as e:
            # we normalize here
            self._json = json.dumps({"result": self.text,
                               "pluginResponse": self._msg})

        except TypeError as e:
            #
            self._json = {"result": self.text,
                               "pluginResponse": self._msg}


        self._html = None

    def json(self):
        return self.success_message(self._msg)

    def __str__(self):
        return self.text

    def html(self):
        return "<H1>Passed</H1>"

    def success_message(self, msg):
        return {"result": "passed", "pluginResponse" :msg}


class Failure(Result):
    """
    base failure object provides a json response child classes may implement more sophisticated response
    """
    def __init__(self, enginemsg):
        """

        :param enginemsg: container output from non-0 exit code
        :return:
        """
        self._msg = enginemsg

        if isinstance(self._msg, ContainerError):
            """
            if we get a containerError, we  need to console output
            """
            self._container_error = self._msg
            self._msg = str(self._msg)

        self._json = None
        self._html = None
        self.text = "Failed"

        # Result Should have valid json, we load it up here
        try:
            self.as_dict = json.loads(enginemsg)
            self._json = enginemsg
        # Except when it doesn't
        except ValueError as e:
            # we normalize here
            self._json = json.dumps({"result": self.text,
                               "pluginResponse": self._msg})

        except TypeError as e:
            #
            self._json = json.dumps({"result": self.text,
                               "pluginResponse": self._msg})


        self._html = None

    def json(self):
        return self.failure_message(self._msg)

    def __str__(self):
        return self.text

    def html(self):
        return "<H1>Failed</H1>"

    def failure_message(self, msg):
        return {"result": "failure", "pluginResponse" :msg}



class ImageNotFoundResponse(Failure):
    """
    Response class / View used when docker is unable find the container image

    e.g ImageNotFound(
    HTTPError(u'404 Client Error: Not Found for url: http+docker://localunixsocket/v1.26/images/create?fromImage=wsldk',),)}
    """
    def __init__(self, enginemsg):
        """
        Response back from docker engine API

        :param enginemsg: container
        :return:
        """
        self._msg = enginemsg
        self._json = None
        self._html = None
        self.text = "Failed - Plugin Not Found"

    def json(self):

        return self._generate_json(self._msg)


    def html(self):
        """
        in the future we can accept html back from container as well
        """

        return "<H1>Failed/NotFound</H1>"

    def _generate_json(self, msg):
        """
        generates json response

        :param msg:
        :return:
        """
        return {"result": "noplugin",
                "pluginResponse": msg
                }


client = docker.from_env()



import logging
import docker
import requests
from docker.errors import ContainerError
import json
import os

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

# Get Results API information from environment raise Exception if the URL is not set
RESULTS_API = os.environ["RESULTS_API"]

RESULTS_API_USER = os.getenv("RESULTS_API_USER", None)
RESULTS_API_PASSWORD = os.getenv("RESULTS_API_PASSWORD", None)

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


class TaskCallback(object):
    """
    TaskCallback is responsible for recieving the response from the celery worker executing a container.

    """

    def __init__(self, jobId, container_msg):
        print("Received Response from container: {}".format(container_msg))
        self._msg_from_container = container_msg
        self.jobId = jobId
        self._upload()

    def _upload(self):
        """
        Send the results to the results API

        :return: requests.Response
        """



        # this needs to move it it's own method
        #result = Result()
        # result = {
        #     "jobId": self.jobId,
        #     "result": "Passed",
        #     "json": None,
        #     "pluginHTMLResponse": "<strong>got job id</strong>"
        # }

        # attaches jobId, ensures we have a good response, otherwise, generates API friendly result
        result = Result(self.jobId, self._msg_from_container)
        # generates json to send to api
        result = result.as_dict()

        print("Uploading Response to Results API")
        resp = requests.post(RESULTS_API, data=result)
        print("Response from API: {}".format(resp.status_code))



class Result(object):

    """
    Result Model

    Input validation and data normalization occurs in this class
    We also attach the jobId to the data so that it can be properly uploaded


    ensures Results data is properly formatted for the results API

        result = {
            "jobId": 15,
            "result": "Passed",
            "json": None,
            "pluginHTMLResponse": "<strong>this is a passed html message</strong>"
        }


    """
    # Fields we must receive from the plugin
    REQUIRED_FIELDS = ("result", "json", "pluginHTMLResponse")

    def __init__(self, jobId, container_msg):

        self.jobId = jobId
        self._container_msg = container_msg

        # check for valid json data
        try:
            self._container_dict = json.loads(self._container_msg)
            print("Got valid json from container: {}".format(self._container_dict))

            # TODO: need to validate required keys are present
            # if all (k in self._container_dict for k in self.REQUIRED_FIELDS):

            # add job id to k,v
            self._container_dict["jobId"] = self.jobId
            self._result_dict = self._container_dict


            # or we do not

        # did not get valid json from container
        except ValueError:
            print("Got bad data from container:  Generating Failure Result")
            self._json = {"jobId": self.jobId,
                          "result": "Failed",
                          "json": {"error": "Error Decoding JSON",
                                   "container_output": self._container_msg},
                          "pluginHTMLResponse": None
                          }


    def as_dict(self):
        return self._result_dict

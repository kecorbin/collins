"""
various results classes that currently are not implemented
"""

# old code
#
#     @classmethod
#     def from_response(cls, jobId=None, result=None, json=None, pluginHTMLResponse=None):
#         """
#         if the plugin generates a result that can be passed through, this can be used as a constructure
#         :param jobId:
#         :param result:
#         :param json:
#         :param pluginHTMLResponse:
#         :return:
#         """
#
#         try:
#             logger.debug("Checking for JSON response from engine response: {}".format(enginemsg))
#             if isinstance(enginemsg, str):
#                 logger.debug("Attempting to load json data")
#                 jsondata = json.loads(enginemsg)
#             elif isinstance(enginemsg, dict):
#                 logger.debug("Creating result from dictionary: {}".format(enginemsg))
#                 jsondata = enginemsg
#                 # the plugin returned proper json, so it should give us a result
#
#             if jsondata['result'] == 'Passed':
#                 logger.debug("Job Marked successfull")
#                 return Success(enginemsg)
#             elif 'result' in jsondata and jsondata['result'] == 'Failed':
#                 logger.debug("Job Marked failed")
#                 return Failure(enginemsg)
#
#         # if we don't get json back the testfailed
#         except ValueError:
#             return Failure(enginemsg)
#
#         except TypeError as e:
#             logger.debug("TYPEERROR {}:".format(e))
#             return Failure(enginemsg)
#
#
#
#
#     pass
# client = docker.from_env()
#
#


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



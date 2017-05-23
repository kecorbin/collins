import requests
import json
import os


# Get Results API information from environment raise Exception if the URL is not set
RESULTS_API = os.environ["RESULTS_API"]

RESULTS_API_USER = os.getenv("RESULTS_API_USER", None)
RESULTS_API_PASSWORD = os.getenv("RESULTS_API_PASSWORD", None)


class TaskCallback(object):
    """
    TaskCallback is responsible for recieving the stdout from the container executed by the celery worker

    """

    def __init__(self, jobid, container_msg):
        print("Received Response from container: {}".format(container_msg))
        self._msg_from_container = container_msg
        self.jobId = jobid
        self._upload()

    def _generate_results(self):
        print("Generating Results")
        # attaches jobId, ensures we have a good response, otherwise, generates API friendly result
        result = Result(self.jobId, self._msg_from_container)
        # generates json to send to api
        results = result.as_dict()
        return results

    def _upload(self):
        """
        Send the results to the results API

        :return: requests.Response
        """
        result = self._generate_results()
        print("Uploading Response to Results API: {}".format(result))
        headers = {"Content-Type": "application/json"}
        resp = requests.post(RESULTS_API, headers=headers, data=json.dumps(result))
        print(resp.text)
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

    def __init__(self, jobid, container_msg):

        self.jobId = jobid
        self._container_msg = container_msg

        # check for valid json data
        try:
            self._container_dict = json.loads(self._container_msg)
            print("Got valid json from container: {}".format(self._container_dict))

            # TODO: we should validate that all required keys are present
            # if all (k in self._container_dict for k in self.REQUIRED_FIELDS):

            # add job id to k,v
            self._container_dict["jobId"] = self.jobId
            #
            self._result_dict = self._container_dict

        # did not get valid json from container
        except ValueError:
            print("Got bad data from container:  Generating Failure Result")
            self._json = {"jobId": self.jobId,
                          "result": "Failed",
                          "json": {"error": "Error Decoding JSON",
                                   "container_output": self._container_msg},
                          "pluginHTMLResponse": None
                          }
            self._result_dict = self._json

    def as_dict(self):
        return self._result_dict

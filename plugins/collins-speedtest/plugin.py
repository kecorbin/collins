#!/usr/bin/env python
################################################################################
#                                                                              #
# Copyright (c) 2015 Cisco Systems                                             #
# All Rights Reserved.                                                         #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License"); you may   #
#    not use this file except in compliance with the License. You may obtain   #
#    a copy of the License at                                                  #
#                                                                              #
#         http://www.apache.org/licenses/LICENSE-2.0                           #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT #
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  #
#    License for the specific language governing permissions and limitations   #
#    under the License.                                                        #
#                                                                              #
################################################################################
"""
always_pass
 This plugin should always pass



"""
import json
import requests
import os

def run_speedtest():
    """
    Main execution routine

    :return: None
    """
    token = os.getenv("JANUS_TOKEN")
    headers = {"Authorization": "Token {}".format(token)}
    payload = {"type": "speedtest"}
    speedtest = requests.post('https://api.interthings.io/api/v1/jobs/', headers=headers, data=payload)

    if speedtest.ok:
        print json.dumps({"result": "Passed",
                              "pluginResponse": speedtest.text,
                              "pluginHTMLResponse": "<h1>Status Code: {}</h1>".format(speedtest.status_code)})
    else:
        print json.dumps({"result": "Failed",
                          "pluginResponse": speedtest.text,
                          "pluginHTMLResponse": "<h1>Status Code: {}</h1>".format(speedtest.status_code)})

if __name__ == "__main__":
    run_speedtest()

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
import os
import json
import subprocess
#from json2html import *

def pinger(target, results):
    devnull = open(os.devnull, 'w')
    if target is None:
        results = ("Failed", "Please make sure and set TARGET in your environment")
        return results
    try:
        out = subprocess.check_call(['ping', '-c1', target],
                              stdout=devnull)

        results = ("Passed", out)

    except Exception as e:
        results = ("Failed", repr(e))

    return results

results = (None, None)

hostname = os.getenv("TARGET", None)
results = pinger(hostname, results)
result, response = results


print json.dumps({"result": result,
                  "pluginResponse": response,
                  "pluginHTMLResponse": "<h1>{}</h1><p>{}</p>".format(result,
                                                                      response),
                  }
                 )

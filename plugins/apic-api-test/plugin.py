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
apic_api_check

 Tests whether the APIC API is available and can be authetnticated



"""
import sys
import os
import json
from acitoolkit.acitoolkit import Tenant, AppProfile, Context, EPG, BridgeDomain, Contract
from acitoolkit.acitoolkit import Credentials, Session
import argparse
import ipaddress

# some useful flags for debugging can be set by environment
DEBUG = os.environ.get('DEBUG', False)
LIVE = os.environ.get('LIVE', True)
STATIC_RESULT = os.environ.get('STATIC_RESULT', 'Failed')


class Checker(object):
    """
    Loosely based on the ACI toolkit acilint.py application
    """
    def __init__(self, session, output, fh=None):
        self.tenants = Tenant.get_deep(session)
        self.output = output
        self.file = fh
        self.result = "Passed"

    def execute(self, methods):
        for method in methods:
            getattr(self, method)()

    def output_handler(self, msg):
        """
        Print(the supplied string in a format appropriate to the output medium.)

        :param msg: The message to be printed.
        """
        # If we've hit the output handler, we know that one of our tests has failed
        self.result = "Failed"
        if self.output == 'console':
            print(msg)

        elif self.output == 'html':

            color_map = {'Error': '#FF8C00',
                         'Critical': '#FF0000',
                         'Warning': '#FFFF00'}

            sev = msg.split(':')[0].split(' ')[0]
            rule = msg.split(':')[0].split(' ')[1]
            descr = msg.split(': ')[1]
            self.file.write("""
            <tr>
            <td bgcolor="{0}">{1}</td>
            <td bgcolor="{0}">{2}</td>
            <td bgcolor="{0}">{3}</td>
            </tr>
            """.format(color_map[sev], sev, rule, descr))





def acilint():
    """
    Main execution routine

    :return: None
    """
    description = ('acilint - A static configuration analysis tool. '
                   'Checks can be individually disabled by generating'
                   ' and editing a configuration file.  If no config '
                   'file is given, all checks will be run.')
    creds = Credentials('apic', description)

    # this should get the creds from environment
    # Login to APIC
    session = Session(os.environ['APIC_URL'], os.environ['APIC_LOGIN'], os.environ['APIC_PASSWORD'])
    resp = session.login()
    html = None
    checker = Checker(session, 'html', html)

    if not resp.ok:
        checker.output_handler('%% Could not login to APIC')
        sys.exit(1)
    else:
        msg = "Successfully able to authenticate to the APIC APIC with status code {}".format(resp.status_code)
        print json.dumps({"result": "Passed",
                          "pluginResponse": msg,
                          "pluginHTMLResponse": "<h1>{}</h1>".format(msg)})
        
if __name__ == "__main__":
    acilint()
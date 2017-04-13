#!/usr/bin/env python
################################################################################
#                        _    ____ ___   _     _       _                       #
#                       / \  / ___|_ _| | |   (_)_ __ | |_                     #
#                      / _ \| |    | |  | |   | | '_ \| __|                    #
#                     / ___ \ |___ | |  | |___| | | | | |_                     #
#                    /_/   \_\____|___| |_____|_|_| |_|\__|                    #
#                                                                              #
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
acilint - A static configuration analysis tool for examining ACI Fabric
          configuration for potential problems and unused configuration.
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


    def warning_001(self):
        """
        W001: Tenant has no app profile
        """
        for tenant in self.tenants:
            if len(tenant.get_children(AppProfile)) == 0:
                self.output_handler("Warning 001: Tenant '%s' has no Application "
                                    "Profile." % tenant.name)

    def warning_002(self):
        """
        W002: Tenant has no context
        """
        for tenant in self.tenants:
            if len(tenant.get_children(Context)) == 0:
                self.output_handler("Warning 002: Tenant '%s' has no Context." % tenant.name)

    def warning_003(self):
        """
        W003: AppProfile has no EPGs
        """
        for tenant in self.tenants:
            for app in tenant.get_children(AppProfile):
                if len(app.get_children(EPG)) == 0:
                    self.output_handler("Warning 003: AppProfile '%s' in Tenant '%s'"
                                        "has no EPGs." % (app.name, tenant.name))

    def warning_004(self):
        """
        W004: Context has no BridgeDomain
        """
        for tenant in self.tenants:
            contexts = []
            for context in tenant.get_children(Context):
                contexts.append(context.name)
            for bd in tenant.get_children(BridgeDomain):
                if bd.has_context():
                    context = bd.get_context().name
                    if context in contexts:
                        contexts.remove(context)
            for context in contexts:
                self.output_handler("Warning 004: Context '%s' in Tenant '%s' has no "
                                    "BridgeDomains." % (context, tenant.name))

    def warning_005(self):
        """
        W005: BridgeDomain has no EPGs assigned
        """
        for tenant in self.tenants:
            bds = []
            for bd in tenant.get_children(BridgeDomain):
                bds.append(bd.name)
            for app in tenant.get_children(AppProfile):
                for epg in app.get_children(EPG):
                    if epg.has_bd():
                        bd = epg.get_bd().name
                        if bd in bds:
                            bds.remove(bd)
            for bd in bds:
                self.output_handler("Warning 005: BridgeDomain '%s' in Tenant '%s'"
                                    " has no EPGs." % (bd, tenant.name))

    def warning_006(self):
        """
        W006: Contract is not provided at all.
        """
        for tenant in self.tenants:
            contracts = []
            for contract in tenant.get_children(Contract):
                contracts.append(contract.name)
            for app in tenant.get_children(AppProfile):
                for epg in app.get_children(EPG):
                    provided = epg.get_all_provided()
                    for contract in provided:
                        if contract.name in contracts:
                            contracts.remove(contract.name)
            for contract in contracts:
                self.output_handler("Warning 006: Contract '%s' in Tenant '%s' is not"
                                    " provided at all." % (contract, tenant.name))

    def warning_007(self):
        """
        W007: Contract is not consumed at all.
        """
        for tenant in self.tenants:
            contracts = []
            for contract in tenant.get_children(Contract):
                contracts.append(contract.name)
            for app in tenant.get_children(AppProfile):
                for epg in app.get_children(EPG):
                    consumed = epg.get_all_consumed()
                    for contract in consumed:
                        if contract.name in contracts:
                            contracts.remove(contract.name)
            for contract in contracts:
                self.output_handler("Warning 007: Contract '%s' in Tenant '%s' is not"
                                    " consumed at all." % (contract, tenant.name))

    def warning_008(self):
        """
        W008: EPG providing contracts but in a Context with no enforcement.
        """
        for tenant in self.tenants:
            for app in tenant.get_children(AppProfile):
                for epg in app.get_children(EPG):
                    if len(epg.get_all_provided()):
                        if epg.has_bd():
                            bd = epg.get_bd()
                            if bd.has_context():
                                context = bd.get_context()
                                if context.get_allow_all():
                                    self.output_handler("Warning 008: EPG '%s' providing "
                                                        "contracts in Tenant '%s', App"
                                                        "Profile '%s' but Context '%s' "
                                                        "is not enforcing." % (epg.name,
                                                                               tenant.name,
                                                                               app.name,
                                                                               context.name))

    def warning_010(self):
        """
        W010: EPG providing contract but consuming EPG is in a different
              context.
        """
        provide_db = {}
        for tenant in self.tenants:
            for app in tenant.get_children(AppProfile):
                for epg in app.get_children(EPG):
                    if epg.has_bd():
                        bd = epg.get_bd()
                        if bd.has_context():
                            context = bd.get_context()
                        provided = epg.get_all_provided()
                        for contract in provided:
                            if tenant.name not in provide_db:
                                provide_db[tenant.name] = {}
                            if contract.name not in provide_db[tenant.name]:
                                provide_db[tenant.name][contract.name] = []
                            if context.name not in provide_db[tenant.name][contract.name]:
                                provide_db[tenant.name][contract.name].append(context.name)

        for tenant in self.tenants:
            if tenant.name not in provide_db:
                self.output_handler("Warning 010: No contract provided within"
                                    " this tenant '%s'" % tenant.name)
                continue  # don't repeat this message for each option below.
            epgs = []
            for app in tenant.get_children(AppProfile):
                for epg in app.get_children(EPG):
                    epgs.append(epg)
            for epg in epgs:
                if epg.has_bd():
                    bd = epg.get_bd()
                    if bd.has_context():
                        context = bd.get_context()
                    consumed = epg.get_all_consumed()
                    for contract in consumed:
                        if contract.name not in provide_db[tenant.name]:
                            self.output_handler("Warning 010: Contract '%s' not provided "
                                                "within the same tenant "
                                                "'%s'" % (contract.name, tenant.name))
                        elif context.name not in provide_db[tenant.name][contract.name]:
                            self.output_handler("Warning 010: Contract '%s' not provided in context '%s' "
                                                "where it is being consumed for"
                                                " tenant '%s'" % (contract.name, context.name, tenant.name))

    def error_001(self):
        """
        E001: BridgeDomain has no Context
        """
        for tenant in self.tenants:
            for bd in tenant.get_children(BridgeDomain):
                if not bd.has_context():
                    self.output_handler("Error 001: BridgeDomain '%s' in tenant '%s' "
                                        "has no Context assigned." % (bd.name, tenant.name))



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
    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(1)


    html = open("tmp.html", "w")
    checker = Checker(session, 'html', html)

    methods = []
    for method in dir(Checker):
        if method.startswith(('warning_', 'error_', 'critical_')):
            methods.append(method)

    if LIVE:

        html.write("""

            <table border="2" style="width:100%">
            <tr>
            <th>Severity</th>
            <th>Rule</th>
            <th>Description</th>
            </tr>
            """)
        checker.execute(methods)

        html.close()
        with open('tmp.html','r') as html:
            #

            resp = {"result": checker.result,
                   "pluginHTMLResponse": html.read()}
            print json.dumps(resp)
    else:
        print json.dumps({"result": STATIC_RESULT})

if __name__ == "__main__":
    acilint()
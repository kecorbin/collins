#!/usr/bin/env python
import os
import json
import subprocess

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

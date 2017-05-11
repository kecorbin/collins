import threading
import subprocess
import sys
import time
import os
import requests
import json


class SchedulerThread(threading.Thread):
    """
    A SchedulerThread is an instance of the celery beat service
    which will monitor a provided API, and restart if requested

    """

    def __init__(self, api, scheduler_name='default', scheduler_id=1):
        """
        :param api: api to check for restart signal e.g http://localhost:8000/api/v1
        :argument scheduler_name the scheduler name, defaults to 'default'
        :argument scheduler_id int the scheduler id, defaults to 1

        :return:
        """
        super(SchedulerThread, self).__init__()
        self.daemon = True
        self.api = api
        self.scheduler_name = scheduler_name
        self.scheduler_id = scheduler_id
        self.scheduler_url = "{}{}".format(self.api, self.scheduler_id)
        print("Using scheduler_url: {}".format(self.scheduler_url))
        self._process = None
        self.need_restart = False

        # celery -A api beat -l info -S django
        self.cmd = [
            'celery', '-A', 'api', 'beat', '-l', 'info',
            '-S', 'django'
        ]

    def _start(self):
        print("Celery Thread is starting")
        try:
            print("Checking for pid file..")
            # cleanup pid file
            if os.remove('celerybeat.pid') is None:
                print("Removed pid file")
        except OSError:
            print("no existing pid file found")

        self._process = subprocess.Popen(self.cmd)

    def _stop(self):
        print("Celery Thread is being shutdown")
        self._process.terminate()

    def mark_as_restarted(self):
        print("Marking restart as completed....."),
        try:
            payload = {"restart": False,
                       "name": "default"}
            resp = requests.put(self.scheduler_url,
                                data=json.dumps(payload),
                                headers={"Content-Type": "application/json"})
            if resp.ok:
                print("OK")
            else:
                print(resp.text)

        except Exception as e:
            print("Failed to mark restart complete, error was: {}".format(e))

    def check_for_restart(self):
        try:
            resp = requests.get(self.scheduler_url)
            print resp.text
            self.need_restart = resp.json()['restart']

        except Exception as e:
            print("Couldn't contact API, we'll stay running: {}".format(e))
            pass

    def run(self):
        self._start()
        while True:
            time.sleep(10)
            print("Checking to see if a restart is requested by the API....."),

            self.check_for_restart()

            if self.need_restart:
                print("restart requested by API")
                self.restart()
            else:
                print("none required")

    def restart(self):
        print("Restarting Celery Thread")
        self._stop()
        self._start()
        self.mark_as_restarted()

try:
    SCHEDULER_API = os.environ["SCHEDULER_API"]

except KeyError:
    print("SCHEDULER_API not found in current API")
    sys.exit(1)

me = SchedulerThread(SCHEDULER_API)
me.run()

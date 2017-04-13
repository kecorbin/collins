from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from client.client import Job

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collins.settings.dev')
app = Celery('api')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def ping(self):
    return "Pong"

@app.task(bind=True)
def add(self, x, y):
    return x + y

@app.task(bind=True, ignore_result=False)
def execute_job(self, job):
    print("Executing Job {}".format(job['id']))
    job = Job(json=job)
    result = job.execute()
    print(result)
    print("Job results are ready")
    return result.json()

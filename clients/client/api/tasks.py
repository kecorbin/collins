from __future__ import absolute_import, unicode_literals
import docker
from celery import Celery
import os
from .callbacks import TaskCallback

app = Celery('tasks', broker=os.getenv('RABBITMQ_URL'),
             )

@app.task(bind=True)
def ping(self):
    return "Pong"

@app.task
def run_image(jobId, image, command=None, **kwargs):
    print("Executing Task for job id {}".format(jobId))
    client = docker.from_env()
    celery_result = client.containers.run(image, command=command, environment=kwargs)
    # we need to pass jobid to the callback
    collins_result = TaskCallback(jobId, celery_result)
    return celery_result

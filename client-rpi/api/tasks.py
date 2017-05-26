from __future__ import absolute_import, unicode_literals
import docker
from docker import Client
from celery import Celery
import os
import json

from .callbacks import TaskCallback

app = Celery('tasks', broker=os.getenv('RABBITMQ_URL'),
             )

@app.task(bind=True)
def ping(self):
    return "Pong"

@app.task
def run_image(jobId, image, command=None, **kwargs):
    print("Executing Task for job id {}".format(jobId))
    client = Client(base_url='unix://var/run/docker.sock') 
    # older versions of docker-py don't pull the image on start/run
    client.pull(image)
    container = client.create_container(image, command=None, environment=kwargs) 

    celery_result = client.start(container)
    container_output = client.logs(container, stdout=True, stderr=True) 
    # we need to pass jobid to the callback
    collins_result = TaskCallback(jobId, container_output)
    return celery_result
from __future__ import absolute_import, unicode_literals
import docker
from celery import Celery
import os


app = Celery('tasks', broker=os.getenv('RABBITMQ_URL'))

@app.task(bind=True)
def ping(self):
    return "Pong"

@app.task(bind=True)
def add(self, x, y):
    return x + y

@app.task
def run_image(image, command=None, **kwargs):
    client = docker.from_env()
    container_output = client.containers.run(image, command=command, **kwargs)
    return container_output


from __future__ import absolute_import, unicode_literals
from .celery import app
import docker
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collins.settings.dev')


@app.task(bind=True)
def ping(self):
    return "Pong"


@app.task(bind=True)
def add(self, x, y):
    return x + y


@app.task
def run_image(jobId, image, command=None, **kwargs):
    client = docker.from_env()
    container_output = client.containers.run(image, command=command, **kwargs)
    return container_output

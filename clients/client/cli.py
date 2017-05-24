# can be pasted into interpreter for an interactive session with the broker/backend
import docker
from celery import Celery
import os


app = Celery('tasks', broker=os.getenv('RABBITMQ_URL'),
                      includes=['api.tasks']
             )

import api.tasks

## results = api.tasks.run_image.apply_async(args=['docker/whalesay'], kwargs={"command":"cowsay moo"}, queue="SITE_1")

from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collins.settings.dev')

# noinspection PyTypeChecker
app = Celery('api.tasks',
             broker=os.getenv('RABBITMQ_URL'),
             backend=os.getenv("REDIS_URL"),
             include=['api.tasks'])


app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()

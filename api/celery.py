from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collins.settings.dev')

app = Celery('proj',
             broker=os.getenv('RABBITMQ_URL'),
             include=['api.tasks'])

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()


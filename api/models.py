# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import jsonfield
from html_field.db.models import HTMLField
from html_field import html_cleaner
from django_celery_beat.models import PeriodicTask

safe_tags = html_cleaner.HTMLCleaner(allow_tags=['a', 'img', 'em', 'strong'])


class Environment(models.Model):
    """
    Base class for info passed to the plugin
    """
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    json = jsonfield.JSONField(max_length=512, null=True, blank=False)

    class Meta:
        unique_together = ('name', 'description', 'json')


class Job(PeriodicTask):
    type = models.CharField(max_length=25, default="DockerJob")
    last_result = models.CharField(max_length=10, default="Fail")
    environment = models.ForeignKey(Environment,
                                    blank=True, null=True, default=None)



class DockerJob(Job):
    image = models.CharField(max_length=128)

    class JSONAPIMeta:
        resource_name = "job"

class Schedule(models.Model):
    pass


class Result(models.Model):
    job = models.ForeignKey(DockerJob,
                            related_name='results',
                            on_delete=models.CASCADE,
                            null=True
                            )
    created = models.DateTimeField(auto_now_add=True)
    jobId = models.IntegerField(null=False,
                                blank=False
                                )
    result = models.CharField(max_length=10)

    json = jsonfield.JSONField(max_length=512,
                               null=True,
                               blank=False
                               )

    pluginHTMLResponse = HTMLField(safe_tags,
                                   null=True,
                                   blank=False
                                   )

    pluginRawResponse = models.TextField(blank=True,
                                         null=True
                                         )

    class Meta:
        ordering = ['-created',]

    def __repr__(self):
        return str(self.id)

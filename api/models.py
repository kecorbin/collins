# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import jsonfield
from html_field.db.models import HTMLField
from html_field import html_cleaner


safe_tags = html_cleaner.HTMLCleaner(allow_tags=['a', 'img', 'em', 'strong'])

class FabricTarget(models.Model):
    """
    a  FabricTarget represents an ACI we will run tests against
    """
    plugin_prefix = models.CharField(max_length=25, default="aci")
    APIC_LOGIN = models.CharField(max_length=25, default='admin')
    APIC_PASSWORD = models.CharField(max_length=25)
    APIC_URL = models.URLField(max_length=25)

    def __str__(self):
        return self.APIC_URL


class Job(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25, default="DockerJob")
    active = models.BooleanField(default=True)
    last_result = models.CharField(max_length=10, default="Fail")
    environment = models.ForeignKey(FabricTarget, blank=True, null=True, default=None)


class DockerJob(Job):
    image = models.CharField(max_length=25)


class Schedule(models.Model):
    pass


class Result(models.Model):
    job = models.ForeignKey(DockerJob, related_name='results', on_delete=models.CASCADE, null=True)
    jobId = models.IntegerField(null=False, blank=False)
    result = models.CharField(max_length=10)
    json = jsonfield.JSONField(max_length=512, null=True, blank=False)
    pluginHTMLResponse = HTMLField(safe_tags, null=True, blank=False)





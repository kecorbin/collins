# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from connect.models import Gateway

class BootFlag(models.BooleanField):

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value) # return 0/1


class System(models.Model):
    """
    A System is a group of devices with or without a controller
    """
    gateway = models.ForeignKey(Gateway, null=True, blank=True)
    job_name = models.CharField(max_length=25)
    system_id = models.CharField(unique=True, max_length=25)
    ctl_mfg = models.CharField(max_length=25, default='unknown')
    mod_version = models.CharField(max_length=25, default='unknown')
    boot_flag = BootFlag()


    def __unicode__(self):
        return str(self.job_name)


class Device(models.Model):
    gateway = models.ForeignKey(Gateway, null=True, blank=True)
    system = models.ForeignKey(System, null=True, blank=True)
    dev_name = models.CharField(max_length=25)
    firmware = models.CharField(max_length=25)
    ip = models.CharField(max_length=25)
    mfg = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    note = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    uniqueid = models.CharField(max_length=25)
    system = models.ForeignKey(System, null=True)

    def __unicode__(self):
        return str(self.dev_name)

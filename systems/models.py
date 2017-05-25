# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BootFlag(models.BooleanField):

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value) # return 0/1


class System(models.Model):
    """
    A Greenlight System with some extensions
    """

    boot_flag = BootFlag()
    ctl_mfg = models.CharField(max_length=25)
    job_name = models.CharField(max_length=25)
    mod_version = models.CharField(max_length=25)
    system_id = models.CharField(max_length=25)

class Device(models.Model):
    dev_name = models.CharField(max_length=25)
    firmware = models.CharField(max_length=25)
    ip = models.CharField(max_length=25)
    mfg = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    note = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    uniqueid = models.CharField(max_length=25)
    system = models.ForeignKey(System, null=True)
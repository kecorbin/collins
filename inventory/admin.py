# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import Device, System


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('boot_flag', 'ctl_mfg', 'job_name', 'mod_version', 'system_id',)
    search_display = ('boot_flag', 'ctl_mfg', 'job_name', 'mod_version', 'system_id',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('dev_name', 'firmware', 'ip', 'mfg', 'model',
                    'note', 'status', 'uniqueid',)
    search_display = ('dev_name', 'firmware', 'ip', 'mfg', 'model',
                      'note', 'status', 'uniqueid',)


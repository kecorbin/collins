# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from api.models import DockerJob, Result, Environment, Scheduler
from django_celery_beat.admin import PeriodicTask, CrontabSchedule


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'json',)


@admin.register(DockerJob)
class DockerJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'enabled', 'environment', 'image',)
    search_fields = ('id', 'image',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(DockerJobAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['task'].initial = 'api.tasks.run_image'
        return form


@admin.register(Result)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobId', 'result',)


@admin.register(Scheduler)
class SchedulerAdmin(admin.ModelAdmin):
    #list_display = ('id', 'name', 'restart')

    def is_something(self, instance):
        if instance.restart == False:
            return False
        return True

    is_something.boolean = True
    is_something.short_description = u"Restart Needed?"

    list_display = ['id', 'name', 'is_something']


# not needed on admin site as DockerJob inherits from PeriodicTask
admin.site.unregister(PeriodicTask)

# crontabs are not currently supported
admin.site.unregister(CrontabSchedule)

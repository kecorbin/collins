# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from api.models import DockerJob, Result, Environment

@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'json',)


@admin.register(DockerJob)
class DockerJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'active', 'environment', 'image',)
    search_fields = ('id', 'image',)


@admin.register(Result)
class ResponseAdmin(admin.ModelAdmin):
    list_display= ('id', 'jobId', 'result',)
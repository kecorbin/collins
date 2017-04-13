# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from api.models import DockerJob, Result, FabricTarget

@admin.register(FabricTarget)
class FabricTargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'APIC_URL', 'APIC_LOGIN', 'APIC_PASSWORD',)


@admin.register(DockerJob)
class DockerJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'active', 'environment', 'image',)
    search_fields = ('id', 'image',)


@admin.register(Result)
class ResponseAdmin(admin.ModelAdmin):
    list_display= ('id', 'jobId', 'result',)
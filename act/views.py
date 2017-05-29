# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from models import DockerJob, Result, Environment, Scheduler, Plugin
from serializers import (ResultsSerializer,
                         DockerJobSerializer,
                         EnvironmentSerializer,
                         IntervalScheduleSerializer,
                         SchedulerSerializer,
                         PluginSerializer
                         )
from django_celery_beat.models import IntervalSchedule

# Create your views here.


class EnvironmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()


class IntervalScheduleViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        get a interval schedule

    list:
        list interval schedules

    create:
        create an interval schedule

    delete:
        delete an interval schedule

    partial_update:
        update fields on an interval schedule

    update:
        update an interval schedule
    """

    serializer_class = IntervalScheduleSerializer
    queryset = IntervalSchedule.objects.all()


class JobViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        get a job

    list:
        list all jobs

    create:
        create a job

    delete:
        delete a job

    partial_update:
        update fields on a job

    update:
        update a job
    """
    serializer_class = DockerJobSerializer
    queryset = DockerJob.objects.all()


class JobResultViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin):
    """
    retrieve:
        get a job result

    list:
        list all job results

    create:
        create a job result

    delete:
        delete a job result

    partial_update:
        update fields on a job result

    update:
        update a job result
    """


    serializer_class = ResultsSerializer
    queryset = Result.objects.all()

    def list(self, request, job_pk=None):
        job = DockerJob.objects.filter(pk=int(job_pk))[0]
        queryset = job.results.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, job_pk=None):
        print "retrieve"
        job = DockerJob.objects.filter(pk=int(job_pk))[0]
        queryset = job.results.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ResultViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for working with results.
    """
    serializer_class = ResultsSerializer
    queryset = Result.objects.all()


class SchedulerViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for working with Schedulers.
    """
    serializer_class = SchedulerSerializer
    queryset = Scheduler.objects.all()

class PluginViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for working with Plugins.
    """
    serializer_class = PluginSerializer
    queryset = Plugin.objects.all()
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework import filters
from models import DockerJob, Result, FabricTarget
from serializers import ResultsSerializer, DockerJobSerializer, FabricTargetSerializer
# Create your views here.

class FabricTargetViewSet(viewsets.ModelViewSet):
    serializer_class = FabricTargetSerializer
    queryset = FabricTarget.objects.all()


class JobViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for working with jobs.
    """
    serializer_class = DockerJobSerializer
    queryset = DockerJob.objects.all()
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('processed', 'type',)
    #permissions_classes = (permissions.IsAuthenticated,)



class ResultViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for working with jobs.
    """
    serializer_class = ResultsSerializer
    queryset = Result.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('jobId',)
    #permissions_classes = (permissions.IsAuthenticated,)

    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     """
    #     Return a list of all the gateways for the current user
    #     """
    #     user = self.request.user
    #     return Job.objects.filter(user=user)
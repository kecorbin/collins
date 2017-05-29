from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from models import Scan, SpeedTest
import json
import serializers
import logging

logger = logging.getLogger(__name__)

# API VIEWS

class ScanViewSet(viewsets.ModelViewSet):
    """
    Scan
    retrieve:
        get a scan

    list:
        get all scans

    create:
        create a scan

    delete:
        delete a scan

    partial_update:
        update fields on a scan

    update:
        update a scan
    """
    serializer_class = serializers.ScanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('processed', 'type',)
    permissions_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Return a list of all the gateways for the current user
        """
        user = self.request.user
        return Scan.objects.filter(user=user)


class SpeedTestViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        get a speed test

    list:
        list all speed tests

    create:
        create a speed test

    delete:
        delete a speed test

    partial_update:
        update fields on a speed test

    update:
        update a speed test
    """
    serializer_class = serializers.SpeedTestSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('processed', 'type',)
    permissions_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Return a list of all the gateways for the current user
        """
        user = self.request.user
        return SpeedTest.objects.filter(user=user)



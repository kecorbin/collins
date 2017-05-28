# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from models import System, Device
import serializers


class SystemViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for working with systems.

    A system is a group of devices which may or may not have a controller associated with them
    """
    serializer_class = serializers.SystemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permissions_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        """
        Return a list of all the gateways for the current user
        """
        # user = self.request.user
        # return System.objects.filter(user=user)
        return System.objects.all()

class DeviceViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for working with systems.

    A system is a group of devices which may or may not have a controller associated with them
    """
    serializer_class = serializers.DeviceSerializer
    permissions_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    # def perform_create(self, serializer):
    #     # serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Return a list of all the gateways for the current user
        """
        # user = self.request.user
        # return Device.objects.filter(user=user)
        return Device.objects.all()
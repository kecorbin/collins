# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from models import System, Device
import serializers


class SystemViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        get a system

    list:
        list all systems

    create:
        create a system

    delete:
        delete a system

    partial_update:
        update fields on a system

    update:
        update a system
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
    retrieve:
        get a device

    list:
        list all devices

    create:
        create a device

    delete:
        delete a device

    partial_update:
        update fields on a device

    update:
        update a device
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
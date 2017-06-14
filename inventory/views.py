# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from models import System, Device
from connect.models import Gateway
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

    def get_queryset(self, **kwargs):
        gateway = Gateway.objects.get(hostname=self.kwargs['gateway_hostname'])
        # make sure user is authorized to use this gateway
        if self.request.user.has_perm('connect.view_gateway', gateway):
            tunnels = System.objects.filter(gateway=gateway)
            return tunnels
        else:
            raise Http404


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

    def get_queryset(self, **kwargs):
        gateway = Gateway.objects.get(hostname=self.kwargs['gateway_hostname'])
        # make sure user is authorized to use this gateway
        if self.request.user.has_perm('connect.view_gateway', gateway):
            tunnels = Device.objects.filter(gateway=gateway)
            return tunnels
        else:
            raise Http404

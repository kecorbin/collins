from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework import filters
from rest_framework import permissions
from models import Scan, SpeedTest
from connect.models import Gateway
from django.http import Http404

import json
import serializers
import logging

logger = logging.getLogger(__name__)

# API VIEWS


class ScanViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,):
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
    queryset = Scan.objects.all()
    filter_fields = ('processed',)

    def list(self, request, gateway_hostname=None):
        """
        get all tunnels for a gateway
        :param request:
        :param gateway_id: str id for the gateway
        :return:
        """
        gateway = Gateway.objects.get(hostname=gateway_hostname)
        # make sure user is authorized to use this gateway
        print self.request.user.has_perm('connect.view_gateway', gateway)
        if self.request.user.has_perm('connect.view_gateway', gateway):
            scans = Scan.objects.filter(gateway=gateway)
            serializer = self.get_serializer(scans, many=True)
            return Response(serializer.data)
        else:
            raise Http404

    def retrieve(self, request, gateway_id=None, pk=None):
        """
        get tunnel details
        :param request:
        :param gateway_id:
        :return:
        """
        scans = Scan.objects.filter(pk=pk, gateway=gateway_id)
        # queryset = Result.results.all()
        serializer = self.get_serializer(scans, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        gateway = Gateway.objects.get(hostname=self.request.data['gateway'])
        serializer.save(gateway=gateway, user=self.request.user)



class SpeedTestViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.CreateModelMixin,):
    """
    retrieve:
        get details about a speedtest

    list:
        get all speedtests for gateway

    create:
        create a speedtest

    delete:
        delete a speedtest

    partial_update:
        update a speedtest prop

    update:
        update a speedtest
    """


    serializer_class = serializers.SpeedTestSerializer
    queryset = SpeedTest.objects.all()
    filter_fields = ('processed',)

    def list(self, request, gateway_hostname=None):
        """
        get all speedtests for a gateway
        :param request:
        :param gateway_id: str id for the gateway
        :return:
        """
        gateway = Gateway.objects.get(hostname=gateway_hostname)
        print gateway
        # make sure user is authorized to use this gateway
        print self.request.user.has_perm('connect.view_gateway', gateway)
        if self.request.user.has_perm('connect.view_gateway', gateway):
            speedtests = SpeedTest.objects.filter(gateway=gateway)
            print speedtests
            serializer = self.get_serializer(speedtests, many=True)
            return Response(serializer.data)
        else:
            raise Http404

    def retrieve(self, request, gateway_hostname=None, pk=None):
        """
        get speedtest details
        :param request:
        :param gateway_id:
        :return:
        """
        speedtests = SpeedTest.objects.filter(pk=pk, gateway=gateway_hostname)
        # queryset = Result.results.all()
        serializer = self.get_serializer(speedtests, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        gateway = Gateway.objects.get(hostname=self.request.data['gateway'])
        serializer.save(gateway=gateway, user=self.request.user)

# class ScanViewSet(viewsets.ModelViewSet):
#     """
#     Scan
#     retrieve:
#         get a scan
#
#     list:
#         get all scans
#
#     create:
#         create a scan
#
#     delete:
#         delete a scan
#
#     partial_update:
#         update fields on a scan
#
#     update:
#         update a scan
#     """
#     serializer_class = serializers.ScanSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ('processed', 'type',)
#     permissions_classes = (permissions.IsAuthenticated,)
#     lookup_field = 'id'
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#     def get_queryset(self):
#         """
#         Return a list of all the gateways for the current user
#         """
#         user = self.request.user
#         return Scan.objects.filter(user=user)
#

# class SpeedTestViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#         get a speed test
#
#     list:
#         list all speed tests
#
#     create:
#         create a speed test
#
#     delete:
#         delete a speed test
#
#     partial_update:
#         update fields on a speed test
#
#     update:
#         update a speed test
#     """
#     serializer_class = serializers.SpeedTestSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ('processed', 'type',)
#     permissions_classes = (permissions.IsAuthenticated,)
#     lookup_field = 'id'
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#     def get_queryset(self):
#         """
#         Return a list of all the gateways for the current user
#         """
#         user = self.request.user
#         return SpeedTest.objects.filter(user=user)



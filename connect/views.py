import logging
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters
from connect import serializers
from connect.helpers import get_client_ip
from connect.models import Tunnel, Gateway, ProxyPort, CloudServer

logger = logging.getLogger(__name__)


def get_user_ip(request):
    print request


'''
Views for Connect API Endpoints
'''


class GatewayViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        get a gateway

    list:
        list all gateways

    create:
        create a gateway

    delete:
        delete a gateway

    partial_update:
        update fields on a gateway

    update:
        update a gateway
    """

    # queryset = Gateway.objects.all()
    serializer_class = serializers.GatewaySerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'hostname'
    def perform_create(self, serializer):
        wanip = get_client_ip(self.request)
        serializer.save(wanip=wanip)

    def get_queryset(self):
        """
        Return a list of all the gateways for the current user
        """
        user = self.request.user
        if user.is_staff:
            qs = Gateway.objects.all()
        else:
            qs = Gateway.objects.filter(user=user)
        return qs

    def update(self, request, *args, **kwargs):
        """
        update a Gateway
        """
        serializer = serializers.GatewaySerializer(data=request.data,
                                                   partial=True)

        if serializer.is_valid():
            # We use the following lines to determine what the gateway is
            # allowed to update on the server side
            obj = self.get_object()
            obj.version = request.data['version']
            obj.pubkey = request.data['pubkey']
            obj.lanip = request.data['lanip']
            obj.mac = request.data['mac']
            # Older gateways may not set the healthy flag
            if 'healthy' in request.data:
                obj.healthy = request.data['healthy']
            else:
                obj.healthy = False
            obj.wanip = get_client_ip(request)
            obj.save()
            serializer = serializers.GatewaySerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DEPRACATED

# class GatewayUpdateView(generics.RetrieveUpdateAPIView):
#     """
#     API Endpoint for Updating Gateway
#     """
#     serializer_class = serializers.GatewaySerializer
#     lookup_field = 'hostname'
#     lookup_url_kwarg = 'hostname'
#
#     def get_queryset(self):
#         """
#         Return a list of all the gateways for the current user
#         """
#         user = self.request.user
#         Gateway.objects.filter(user=user)
#         return Gateway.objects.filter(user=user)
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         serializer = serializers.GatewaySerializer(data=request.data,
#                                                    partial=True)
#
#         if serializer.is_valid():
#             # We use the following lines to determine what the gateway is
#             # allowed to update on the server side
#             obj = self.get_object()
#             obj.version = request.data['version']
#             obj.pubkey = request.data['pubkey']
#             obj.lanip = request.data['lanip']
#             obj.mac = request.data['mac']
#             # Older gateways may not set the healthy flag
#             if 'healthy' in request.data:
#                 obj.healthy = request.data['healthy']
#             else:
#                 obj.healthy = False
#             obj.wanip = get_client_ip(request)
#             obj.save()
#             serializer = serializers.GatewaySerializer(obj)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

class TunnelListViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        get a tunnel

    list:
        list all tunnels

    create:
        create a tunnel

    delete:
        delete a tunnel

    partial_update:
        update fields on a tunnel

    update:
        update a tunnel
    """

    serializer_class = serializers.TunnelsSerializer
    permissions_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('processed',)

    def get_queryset(self):
        """
        Return a list of all the tunnels for the current user
        """

        user = self.request.user
        if user.is_staff:
            qs = Tunnel.objects.all()
        else:
            qs = Tunnel.objects.filter(user=user)
        update_last_login(None, user)
        return qs

    def perform_create(self, serializer):

        # get the source ip address of the request

        # self.request.data will look something like this
        # {u'remoteport': 22, u'remotehost': u'192.168.10.254', u'sourceip': u'173.37.200.6', u'timeout': 5}
        if 'sourceip' not in self.request.data:
            ip = get_client_ip(self.request)

        else:
            ip = self.request.data['sourceip']

        serializer.save(user=self.request.user, sourceip=ip)


class CreateTunnelViewSet(viewsets.ModelViewSet):
    """
    create:
        create a tunnel

    delete:
        delete a tunnel

    partial_update:
        update fields on a tunnel

    update:
        update a tunnel
    """
    serializer_class = serializers.CreateTunnelSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        # dynamically populating source IP address for API calls
        # while still allowing the client to specify,
        # this accounts for two use cases.
        # 1. the API call is being made on behalf of a client, ie, Greenlight
        # 2. the API call is being made by the client itself

        # get the source ip address of the request

        # self.request.data will look something like this
        # {u'remoteport': 22, u'remotehost': u'192.168.10.254', u'sourceip': u'173.37.200.6', u'timeout': 5}
        if 'sourceip' not in self.request.data:
            ip = get_client_ip(self.request)

        else:
            ip = self.request.data['sourceip']

        serializer.save(user=self.request.user, sourceip=ip)

    def get_queryset(self):
        """
        Return a list of all the tunnels for the current user
        """
        user = self.request.user
        Tunnel.objects.filter(user=user)
        return Tunnel.objects.filter(user=user)


class CloudServerViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        get a cloudserver

    list:
        list all cloudservers

    create:
        create a cloudserver

    delete:
        delete a cloudserver

    partial_update:
        update fields on a cloudserver

    update:
        update a cloudserver
    """

    queryset = CloudServer.objects.all()
    serializer_class = serializers.CloudServerSerializer
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('fqdn',)


class ProxyPortViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        get a proxyport

    list:
        list all proxyports

    create:
        create a proxyport

    delete:
        delete a proxyport

    partial_update:
        update fields on a proxyport

    update:
        update a proxyport
    """

    queryset = ProxyPort.objects.all()
    serializer_class = serializers.ProxyPortSerializer
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('proxyport',)

import logging
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import update_last_login
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters

from connect.forms import TunnelForm, ConsoleForm
from connect import serializers
from connect.helpers import get_client_ip
from connect.models import Tunnel, Gateway, ProxyPort, CloudServer
from discover.models import Scan, SpeedTest

logger = logging.getLogger(__name__)


def get_user_ip(request):
    print request


class LoginRequiredMixin(object):
    """
    Mixin with another class to ensure that a user is logged in before
    viewing.
    """

    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'connect/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        # super users get full dashboard

        if self.request.user.is_superuser:
            context['devices'] = Gateway.objects.filter(healthy=False)
            context['online_gw_count'] = Gateway.objects.filter(healthy=True).count()
            context['tunnels_procssed_count'] = Tunnel.objects.count()
            context['jobs_processed_count'] = Job.objects.count()
            context['speedtest_results'] = SpeedTestResult.objects.count()
            context['unhealthy_gw_count'] = Gateway.objects.filter(healthy=False).count()
            context['failed_tunnel_count'] = Job.objects.filter(processed=False).count()
            context['failed_job_count'] = Job.objects.filter(processed=False).count()
            context['cloudserver_count'] = CloudServer.objects.count()
            context['proxport_count'] = ProxyPort.objects.filter(inuse=False)

        else:
            context['devices'] = Gateway.objects.filter(user=self.request.user)

        return context


class GatewayListView(LoginRequiredMixin, ListView):
    model = Gateway
    context_object_name = 'devices'
    template_name = 'connect/gateways.html'

    def get_queryset(self):
        """
        Return a list of all the tunnels for the current user
        """
        user = self.request.user
        if self.request.user.is_superuser:
            qs = Gateway.objects.all()
        else:
            qs = Gateway.objects.filter(user=user)
        return qs


class ConsoleTunnel(LoginRequiredMixin, FormView):
    model = Tunnel
    context_object_name = 'proxy'
    template_name = 'connect/create_console_button.html'
    form_class = ConsoleForm
    success_url = '/console/'

    def get_context_data(self, **kwargs):
        context = super(ConsoleTunnel, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # commit=False so that we can add some non-user exposed options
        tunnel_instance = form.save(commit=False)
        gateway = Gateway.objects.get(user=self.request.user)

        tunnel_instance.cloudserver = gateway.cloudserver
        proxyport = ProxyPort.objects.filter(
                                gateway__isnull=True,
                                cloudserver=gateway.cloudserver).first()
        tunnel_instance.proxyport = proxyport
        tunnel_instance.gateway = gateway
        tunnel_instance.timeout = self.request.POST['timeout']
        tunnel_instance.user = self.request.user

        tunnel_instance.save()
        messages.success(self.request,
                         '{} port {} is now '
                         'reachable at {}'.format(tunnel_instance.remotehost,
                                                  tunnel_instance.remoteport,
                                                  tunnel_instance.proxyport)
                         )

        return render(self.request,
                      'connect/create_console_button.html',
                      {'host': tunnel_instance.cloudserver,
                       'port': tunnel_instance.proxyport})


class TunnelListView(LoginRequiredMixin, FormMixin, ListView):
    model = Tunnel
    context_object_name = 'tunnels'
    template_name = 'connect/tunnels.html'
    form_class = TunnelForm
    success_url = '/tunnels'

    def get_queryset(self):
        """
        Return a list of all the tunnels for the current user
        """
        user = self.request.user
        Gateway.objects.filter(user=user)
        return Tunnel.objects.filter(user=user)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # commit=False so that we can add some non-user exposed options
        tunnel_instance = form.save(commit=False)
        gateway = Gateway.objects.get(user=self.request.user)

        tunnel_instance.cloudserver = gateway.cloudserver
        proxyport = ProxyPort.objects.filter(
                            gateway__isnull=True,
                            cloudserver=gateway.cloudserver).first()
        tunnel_instance.proxyport = proxyport
        tunnel_instance.gateway = gateway
        tunnel_instance.timeout = self.request.POST['timeout']
        tunnel_instance.user = self.request.user
        tunnel_instance.save()
        messages.success(self.request,
                         '{} port {} is now reachable at {}'.format(
                             tunnel_instance.remotehost,
                             tunnel_instance.remoteport,
                             tunnel_instance.proxyport)
                         )
        return HttpResponseRedirect('/tunnels/')


'''
Views for API Endpoints
'''


class GatewayViewSet(viewsets.ModelViewSet):

    """
    API endpoint for working with gateways
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
        PUT is supported for operations like u
        :param request:
        :param args:
        :param kwargs:
        :return:
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
    This endpoint will be deprecated in future release
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
    queryset = CloudServer.objects.all()
    serializer_class = serializers.CloudServerSerializer
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('fqdn',)


class ProxyPortViewSet(viewsets.ModelViewSet):
    queryset = ProxyPort.objects.all()
    serializer_class = serializers.ProxyPortSerializer
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('proxyport',)

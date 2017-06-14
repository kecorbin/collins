from rest_framework.response import Response
from rest_framework import viewsets
from models import Scan, SpeedTest
from connect.models import Gateway
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
    queryset = Scan.objects.all()
    filter_fields = ('processed',)

    def get_queryset(self, **kwargs):
        gateway = Gateway.objects.get(hostname=self.kwargs['gateway_hostname'])
        # make sure user is authorized to use this gateway
        if self.request.user.has_perm('connect.view_gateway', gateway):
            tunnels = Scan.objects.filter(gateway=gateway)
            return tunnels
        else:
            raise Http404

    def retrieve(self, request, gateway_id=None, pk=None):
        """
        get tunnel details
        :param request:
        :param gateway_id:
        :param pk
        :return:
        """
        scans = Scan.objects.filter(pk=pk, gateway=gateway_id)
        # queryset = Result.results.all()
        serializer = self.get_serializer(scans, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        gateway = Gateway.objects.get(hostname=self.request.data['gateway'])
        serializer.save(gateway=gateway, user=self.request.user)


class SpeedTestViewSet(viewsets.ModelViewSet):
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

    def get_queryset(self, **kwargs):
        gateway = Gateway.objects.get(hostname=self.kwargs['gateway_hostname'])
        # make sure user is authorized to use this gateway
        if self.request.user.has_perm('connect.view_gateway', gateway):
            tunnels = SpeedTest.objects.filter(gateway=gateway)
            return tunnels
        else:
            raise Http404

    # def list(self, request, gateway_hostname=None):
    #     """
    #     get all speedtests for a gateway
    #     :param request:
    #     :param gateway_id: str id for the gateway
    #     :return:
    #     """
    #     gateway = Gateway.objects.get(hostname=gateway_hostname)
    #     print gateway
    #     # make sure user is authorized to use this gateway
    #     print self.request.user.has_perm('connect.view_gateway', gateway)
    #     if self.request.user.has_perm('connect.view_gateway', gateway):
    #         speedtests = SpeedTest.objects.filter(gateway=gateway)
    #         print speedtests
    #         serializer = self.get_serializer(speedtests, many=True)
    #         return Response(serializer.data)
    #     else:
    #         raise Http404

    def retrieve(self, request, gateway_hostname=None, pk=None):
        """
        get speedtest details
        :param request:
        :param gateway_hostname
        :param pk:
        :return:
        """
        speedtests = SpeedTest.objects.filter(pk=pk, gateway=gateway_hostname)
        # queryset = Result.results.all()
        serializer = self.get_serializer(speedtests, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        gateway = Gateway.objects.get(hostname=self.request.data['gateway'])
        serializer.save(gateway=gateway, user=self.request.user)

from connect.models import Gateway, Tunnel, CloudServer, ProxyPort
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)


class GatewaySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Gateway
        fields = ('mac', 'lanip', 'wanip', 'hostname', 'user',
                  'pubkey', 'version', 'polling_interval',
                  'upgrade', 'healthy', 'modified')


class CloudServerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CloudServer
        fields = ['fqdn', 'user', 'key', 'id']


class ProxyPortSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the proxyport model.
    """
    # There may be a better way of accomplishing this
    # For details see
    # http://stackoverflow.com/questions/29950956/drf-simple-foreign-key-assignment-with-nested-serializers
    cloudserver = CloudServerSerializer(read_only=True)
    qs = CloudServer.objects.all()
    cloudserver_id = serializers.PrimaryKeyRelatedField(queryset=qs,
                                                        source='cloudserver',
                                                        write_only=True)

    class Meta:
        model = ProxyPort
        partial = True
        fields = ['cloudserver', 'proxyport', 'cloudserver_id']


class TunnelsSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    proxyport = ProxyPortSerializer(partial=True)

    def _user(self, obj):
        user = self.context['request'].user
        return user

    class Meta:
        model = Tunnel
        fields = ['id', 'remotehost', 'remoteport', 'timeout', 'user',
                  'proxyport', 'sourceip', 'processed', 'url', 'created',]


class CreateTunnelSerializer(serializers.HyperlinkedModelSerializer):
    """
    This endpoint will be deprecated in future release
    """
    user = serializers.ReadOnlyField(source='user.username')
    port = serializers.ReadOnlyField(source='proxyport.proxyport')
    server = serializers.ReadOnlyField(source='proxyport.cloudserver.fqdn')

    def _user(self, obj):
        user = self.context['request'].user
        return user

    class Meta:
        model = Tunnel
        fields = ['id', 'remotehost', 'remoteport', 'timeout',
                  'user', 'sourceip', 'port', 'server', ]

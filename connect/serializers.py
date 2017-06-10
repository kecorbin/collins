from connect.models import Gateway, Tunnel, CloudServer, ProxyPort
from rest_framework import serializers
import logging
from guardian.shortcuts import get_objects_for_user
from rest_framework.fields import CurrentUserDefault
logger = logging.getLogger(__name__)

class FilterRelatedMixin(object):
    def __init__(self, *args, **kwargs):
        super(FilterRelatedMixin, self).__init__(*args, **kwargs)
        for name, field in self.fields.iteritems():
            if isinstance(field, serializers.RelatedField):
                method_name = 'filter_%s' % name
                try:
                    func = getattr(self, method_name)
                except AttributeError:
                    pass
                else:
                    field.queryset = func(field.queryset)

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


class TunnelsSerializer(FilterRelatedMixin, serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    proxyport = ProxyPortSerializer(read_only=True)
    port = serializers.ReadOnlyField(source='proxyport.proxyport')
    server = serializers.ReadOnlyField(source='proxyport.cloudserver.fqdn')
    # TODO: not sure if this is needed still with FilterRelated Mixin
    gateway = serializers.SlugRelatedField(slug_field='hostname', queryset=Gateway.objects.all())
    #gateway = serializers.SlugRelatedField(slug_field='hostname', queryset=Gateway.objects.none())
    url = serializers.ReadOnlyField()


    class Meta:
        model = Tunnel
        fields = ['id', 'remotehost', 'remoteport', 'timeout', 'user', 'gateway',
                  'server', 'port', 'sourceip', 'processed', 'url', 'created','proxyport']

    def filter_gateway(self, queryset):
        user = self.context['request'].user
        return get_objects_for_user(user, 'connect.view_gateway', klass=Gateway)

    def _user(self, obj):
        user = self.context['request'].user
        return user


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

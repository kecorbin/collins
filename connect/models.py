from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone
import logging
import requests
import json

logger = logging.getLogger(__name__)


DEFAULT_CLOUD_SERVER = 'connect.greenlightcontrol.com'
# Create your models here.


class TunnelManager(models.Manager):
        """ Query only objects which have not been deleted. """
        def get_queryset(self):
            query_set = super(TunnelManager, self).get_queryset()
            return query_set.filter(deleted__isnull=True)


class TunnelArchiveManager(models.Manager):
        """ Query only objects which have been deleted. """
        def get_queryset(self):
            query_set = super(TunnelArchiveManager, self).get_queryset()
            return query_set.filter(deleted__isnull=False)


class CloudServer(models.Model):
    fqdn = models.CharField(max_length=50,
                            unique=True,
                            default=DEFAULT_CLOUD_SERVER)
    user = models.CharField(max_length=10, default='janus')
    key = models.TextField(max_length=2048)

    def __unicode__(self):
        return self.fqdn


class Gateway(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    mac = models.CharField(max_length=80)
    version = models.CharField(max_length=16, default='unknown')
    lanip = models.GenericIPAddressField(null=True, blank=True)
    # WAN IP will be reset on the server side based on the request
    wanip = models.CharField(max_length=32, default='unknown')
    hostname = models.CharField(max_length=64, unique=True)
    pubkey = models.CharField(max_length=512, null=True, blank=True)
    privkey = models.CharField(max_length=512, null=True, blank=True)
    # TODO: need to implement on_delete REQUIRES DATABASE MIGRATION
    cloudserver = models.ForeignKey(CloudServer, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    # Healthy will be set to true every time the gateway successfully updates itself,
    # Can also be used as a "ping" by setting this to false, and checking for it to
    # return to true
    healthy = models.BooleanField(default=False)
    # Setting Upgrade to True will enable automatic updates for the gateway agent
    upgrade = models.BooleanField(default=False)
    last_tested = models.DateTimeField(auto_now=True, null=True)
    # Polling interval specifies how often the gateway will poll the API for work
    polling_interval = models.SmallIntegerField(default=15)

    def __unicode__(self):
        return str(self.hostname)


class ProxyPort(models.Model):
    cloudserver = models.ForeignKey(CloudServer, null=True, blank=True)
    proxyport = models.IntegerField()
    inuse = models.BooleanField(default=False)

    class Meta:
        unique_together = ('cloudserver', 'proxyport',)

    def is_active(self):
        return self.inuse

    def __unicode__(self):
        return unicode(self.cloudserver) + ":" + unicode(self.proxyport)


class Tunnel(models.Model):
    objects = TunnelManager()
    archived_objects = TunnelArchiveManager()
    user = models.ForeignKey(User, null=True, blank=True)
    gateway = models.ForeignKey(Gateway, null=True, blank=True)
    proxyport = models.OneToOneField(ProxyPort, null=True, blank=True)
    sourceip = models.GenericIPAddressField(default='0.0.0.0')
    remoteport = models.IntegerField()
    remotehost = models.CharField(max_length=128)
    timeout = models.SmallIntegerField(default=30)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(blank=True, null=True)
    processed = models.BooleanField(default=False)
    url = models.URLField(default=None, blank=True, null=True)

    def save(self, *args, **kw):
        # Cleanup proxy port when tunnel is processed
        if self.proxyport and self.processed:
            self.proxyport.inuse = False
            self.proxyport.save()
            self.proxyport = None
        else:
            # create relationship with gateway - this will have to change
            # if we support multiple gw's / user
            self.gateway = Gateway.objects.get(hostname=self.user.username)
            logger.info('{} : Assigning tunnel to gateway {}'.format(self.user.username,
                                                                     self.gateway))

            # Attempt to determine regional cloudserver to use, otherwise use full pool
            if self.gateway.cloudserver is not None:
                logger.info('{} : affinity for cloudserver {}'.format(self.gateway.hostname,
                                                                      self.gateway.cloudserver))
                available_ports = ProxyPort.objects.filter(inuse=False,
                                                           cloudserver=self.gateway.cloudserver)
            else:
                available_ports = ProxyPort.objects.filter(inuse=False)

            pp = available_ports.order_by('?')[:1].get()

            pp.inuse = True
            pp.save()

            self.proxyport = pp
            self.proxyport.save()

        if self.remoteport == 80:
            self.url = 'http://{}/'.format(self.proxyport)
        elif self.remoteport == 443:
            self.url = 'https://{}'.format(self.proxyport)
        elif self.remoteport == 8000:
            self.url = 'http://{}'.format(self.proxyport)
        elif self.remoteport == 22:
            self.url = 'ssh://{}'.format(self.proxyport)
        elif self.remoteport == 23:
            self.url = 'telnet://{}'.format(self.proxyport)
        super(Tunnel, self).save(*args, **kw)
        # Removing this log message for now..

        # logger.info("{} : Assigned proxyport {} "
        #                 "to tunnel id {}".format(self.user.username,
        #                                          self.proxyport,
        #                                          self.id))

        logger.info("{} : Successfully created "
                    "tunnel id {}".format(self.user.username,
                                          self.id))

    def delete(self, trash=True):
        # return proxy port to available pool
        if self.proxyport is not None:
            proxyport = self.proxyport
            proxyport.inuse = False
            proxyport.save()
            self.proxyport = None
        self.deleted = timezone.now()
        self.save()
        logger.info('{} : Deleting Tunnel id {} '.format(self.user.username, self.id))
        super(Tunnel, self).delete()

    def __unicode__(self):
        return str(self.remotehost + ":" + str(self.remoteport))


@receiver(post_save, sender=Gateway)
def create_user_for_gw(sender, instance=None, created=False, **kwargs):

    if created:
        user = User(username=instance.hostname)
        user.set_password(instance.mac)
        user.is_active = True
        user.save()
        logger.info("{} : Created User account".format(instance.hostname))
        # Associate current user with newly created GW
        instance.user = user
        instance.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):

    if created:
        logger.info("{} : Creating Token".format(instance.username))
        Token.objects.create(user=instance)


# Needs to move to a different module
def post_to_cop(tunnel):
    """
    POSTS tunnel object to appropriate cloudserver

    :param tunnel: django tunnel object
    :return: response

    """
    # TODO re-use django serializer here if possible
    headers = {"Content-Type": "application/json"}
    tunnel_dict = {
        "id": tunnel.id,
        "remotehost": tunnel.remotehost,
        "remoteport": tunnel.remoteport,
        "timeout": tunnel.timeout,
        "user": tunnel.user.username,
        "proxyport": {
            "cloudserver": {
                "fqdn": tunnel.proxyport.cloudserver.fqdn,
                "user": tunnel.proxyport.cloudserver.user,
                "key": tunnel.proxyport.cloudserver.key,
                "id": tunnel.proxyport.cloudserver.id
            },
            "proxyport": tunnel.proxyport.proxyport
        },
        "sourceip": tunnel.sourceip,
        "processed": tunnel.processed,
        "url":  tunnel.url
    }

    url = "http://{}/tunnels".format(tunnel_dict['proxyport']
                                     ['cloudserver']['fqdn'])
    try:
        resp = requests.post(url, json.dumps(tunnel_dict), headers=headers)
    except:
        pass

    return resp or None


@receiver(post_save, sender=Tunnel)
def notify_cop_of_tunnel(sender, instance=None, created=False, **kwargs):
    """
    Call REST API for traffic cop to open tunnel in on the
    appropriate cloudserver
    """

    if created:
        logger.info('{} : Notifying cop at {} for '
                    'tunnel id {} to {}:{}'.format
                    (instance.user.username,
                     instance.proxyport.cloudserver.fqdn,
                     instance.id,
                     instance.remotehost,
                     instance.remoteport))

        resp = post_to_cop(instance)
        logger.info('{} : Cop response from {} '
                    'for tunnel id {}: {}'.format
                    (instance.user.username,
                     instance.proxyport.cloudserver.fqdn,
                     instance.id,
                     resp))

from django.db import models
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


class Scan(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    destination = models.CharField(max_length=25, null=True, blank=True)
    ports = models.CharField(max_length=25, null=True, blank=True)
    type = models.CharField(max_length=25)
    id = models.AutoField(primary_key=True)
    results = models.TextField(max_length=512000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    processed = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)


    def save(self, *args, **kw):
        super(Scan, self).save(*args, **kw)
        logger.info('{} : Saving Job id {} - type={}'.format(self.user,
                                                           self.id,
                                                           self.type))

class SpeedTest(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    ports = models.CharField(max_length=25, null=True, blank=True)
    type = models.CharField(max_length=25, default='speedtest')
    id = models.AutoField(primary_key=True)
    results = models.TextField(max_length=512000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    processed = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kw):
        super(SpeedTest, self).save(*args, **kw)
        logger.info('{} : saving speedtest {} - type={}'.format(self.user,
                                                           self.id,
                                                           self.type))


class Host(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    ip = models.GenericIPAddressField()
    os = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastboot = models.CharField(max_length=100, blank=True, null=True)


class Service(models.Model):
    host = models.ForeignKey(Host, null=True, blank=True)
    protocol = models.CharField(blank=True, null=True, max_length=10)
    port = models.PositiveIntegerField(blank=True, null=True)

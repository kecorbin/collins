from django.db import models
from django.contrib.auth.models import User
from connect.models import Gateway
import logging
import jsonfield
logger = logging.getLogger(__name__)


class Scan(models.Model):

    class Meta:
        permissions = (
            ('scans', 'View/Perform network scans'),
        )

    user = models.ForeignKey(User, null=True, blank=True)
    gateway = models.ForeignKey(Gateway, null=True, blank=True)
    destination = models.CharField(max_length=25, null=True, blank=True)
    ports = models.CharField(max_length=25, null=True, blank=True)
    type = models.CharField(max_length=25, default='quick-vendor')
    id = models.AutoField(primary_key=True)
    results = jsonfield.JSONField(max_length=512000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    processed = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kw):
        super(Scan, self).save(*args, **kw)
        logger.info('{} : Updated job {} - type={}'.format(self.user,
                                                           self.id,
                                                           self.type))


    def save(self, *args, **kw):
        super(Scan, self).save(*args, **kw)
        logger.info('{} : Saving Job id {} - type={}'.format(self.user,
                                                           self.id,
                                                           self.type))

class SpeedTest(models.Model):
    class Meta:
        permissions = (
            ('speedtests', 'View/Perform Speedtests'),
        )

    destination = models.CharField(max_length=25, null=True, blank=True)
    ports = models.CharField(max_length=25, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    gateway = models.ForeignKey(Gateway, null=True, blank=True)
    type = models.CharField(max_length=25, default='speedtest')
    results = models.TextField(max_length=16384, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def save(self, *args, **kw):
        super(SpeedTest, self).save(*args, **kw)
        logger.info('{} : Speedtest result for job id {}'.format(self.user,
                                                                 self.id))


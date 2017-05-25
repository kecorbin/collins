from django.db import models
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


class Job(models.Model):
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
        super(Job, self).save(*args, **kw)
        logger.info('{} : Updated job {} - type={}'.format(self.user,
                                                           self.id,
                                                           self.type))


    def save(self, *args, **kw):
        super(Job, self).save(*args, **kw)
        logger.info('{} : Saving Job id {} - type={}'.format(self.user,
                                                           self.id,
                                                           self.type))

class SpeedTestResult(models.Model):
    id = models.IntegerField(primary_key=True)
    destination = models.CharField(max_length=25, null=True, blank=True)
    ports = models.CharField(max_length=25, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    results = models.TextField(max_length=16384, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    job = models.OneToOneField(Job, null=True, blank=True)

    def save(self, *args, **kw):
        # Match the result with the corresponding job
        if Job.objects.filter(id=self.id)[0]:
            self.job = Job.objects.filter(id=self.id)[0]
            self.job.results = self.results
            self.job.save()

        super(SpeedTestResult, self).save(*args, **kw)
        logger.info('{} : Speedtest result for job id {}'.format(self.user,
                                                                 self.id))


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

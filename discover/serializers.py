from rest_framework import serializers
from models import Job, SpeedTestResult
import logging

logger = logging.getLogger(__name__)


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ('type', 'destination', 'ports', 'id', 'results',
                  'processed', 'created', 'modified',)
        partial = True


class SpeedTestResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SpeedTestResult
        fields = ('id', 'results', 'destination', 'ports', 'processed',
                  'job', 'created',)
        partial = True

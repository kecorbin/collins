from rest_framework import serializers
from models import Scan, SpeedTest
import logging

logger = logging.getLogger(__name__)


class ScanSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Scan
        fields = ('type', 'destination', 'ports', 'id', 'results',
                  'processed', 'created', 'modified',)
        partial = True


class SpeedTestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SpeedTest
        fields = ('id', 'results', 'type', 'processed', 'created',)
        partial = True

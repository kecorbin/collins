from rest_framework import serializers
from models import System, Device
import logging

logger = logging.getLogger(__name__)


class SystemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = System
        fields = ('id',
                  'job_name',
                  'system_id',
                  'ctl_mfg',
                  'mod_version',
                  'boot_flag')

        partial = True

    def create(self, validated_data):
        print validated_data

        return System.objects.create(**validated_data)

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'dev_name', 'firmware', 'ip', 'mfg', 'model',
                  'note', 'status', 'uniqueid',)
        partial = True

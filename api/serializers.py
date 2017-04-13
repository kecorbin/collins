from rest_framework import serializers
from api.models import DockerJob, Result, FabricTarget
import logging

logger = logging.getLogger(__name__)

class FabricTargetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FabricTarget
        lookup_field = 'id'
        fields = ('APIC_LOGIN', 'APIC_URL', 'APIC_PASSWORD')

class DockerJobSerializer(serializers.HyperlinkedModelSerializer):
    environment = FabricTargetSerializer(partial=True)
    latest = serializers.ReadOnlyField(source='results.last.results')

    class Meta:
        model = DockerJob
        # fields = ('type', 'destination', 'ports', 'id', 'results',
        #           'processed', 'created', 'modified',)
        partial = True
        # fields = '__all__'
        fields = ('id','name','type','image', 'latest', 'active','last_result', 'environment',)
        lookup_field = 'id'

    def create(self, validated_data):

        env_data = validated_data.pop('environment')
        fab = FabricTarget.objects.get_or_create(env_data)
        return DockerJob.objects.create(environment=fab[0], **validated_data)


class ResultsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Result
        fields = ('id','jobId', 'result', 'json', 'pluginHTMLResponse',)
        lookup_field = 'id'
        # lookup_field = 'response-detail'

    def create(self, validated_data):
        print validated_data
        job = DockerJob.objects.get(id=validated_data['jobId'])
        return Result.objects.create(job=job, **validated_data)

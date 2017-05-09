from rest_framework import serializers
from api.models import DockerJob, Result, Environment
from django_celery_beat.models import IntervalSchedule
import logging
import json
logger = logging.getLogger(__name__)


class IntervalScheduleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IntervalSchedule
        lookup_field = 'id'
        fields = ('id', 'every', 'period',)


class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        partial = True
        model = Environment
        lookup_field = 'id'
        fields = ('id', 'name', 'description', 'json')


class ResultsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Result
        fields = ('id', 'created', 'result', 'json',
                  'pluginHTMLResponse', 'pluginRawResponse', 'jobId')
        lookup_field = 'id'
        # lookup_field = 'response-detail'

    def create(self, validated_data):
        print validated_data
        try:
            job = DockerJob.objects.get(id=validated_data['jobId'])
        except:
            # there may be a better way to handle this,
            # we simply reject the result and log it for now
            print("Could not find job for results")

        job.last_result = validated_data['result']
        job.save()
        return Result.objects.create(job=job, **validated_data)


class DockerJobSerializer(serializers.HyperlinkedModelSerializer):
    environment = EnvironmentSerializer(partial=True, required=False)
    latest = serializers.ReadOnlyField(source='results.last.results')
    interval = IntervalScheduleSerializer(partial=True)
    passed_count = serializers.SerializerMethodField()
    failed_count = serializers.SerializerMethodField()

    class Meta:
        model = DockerJob
        # fields = ('type', 'destination', 'ports', 'id', 'results',
        #           'processed', 'created', 'modified',)
        partial = True
        # fields = '__all__'
        fields = ('id', 'name', 'type', 'image',
                  'latest', 'last_result', 'environment',
                  'enabled', 'interval', 'queue', 'passed_count',
                  'failed_count')

        lookup_field = 'id'

    def get_passed_count(self, obj):
        return obj.results.filter(result="Passed").count()

    def get_failed_count(self, obj):
        return obj.results.filter(result="Failed").count()

    def create(self, validated_data):
        # get interval information from request
        # and match up to existing Interval
        interval_data = validated_data.pop('interval')
        period = interval_data['period']
        every = interval_data['every']
        interval = IntervalSchedule.objects.get_or_create(period=period,
                                                          every=every)[0]

        # get evnrionment information from request
        # and match to existing or create a new one
        if 'environment' in validated_data:
            env_data = validated_data.pop('environment')
            env = Environment.objects.get_or_create(env_data)
            job = DockerJob.objects.create(environment=env[0],
                                           interval=interval,
                                           task='api.tasks.run_image',
                                           **validated_data)
        else:
            job = DockerJob.objects.create(interval=interval,
                                           task='api.tasks.run_image',
                                           **validated_data)

        # save is so that we can get primary key
        job.refresh_from_db()
        job.args = json.dumps([job.id, job.image])
        job.save()
        return job

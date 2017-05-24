from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from models import Job, SpeedTestResult
from forms import JobForm
import json
import serializers
import logging

logger = logging.getLogger(__name__)


class LoginRequiredMixin(object):
    """
    Mixin with another class to ensure that a user is logged in before
    viewing.
    """
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)

# UI VIEWS


class JobListView(LoginRequiredMixin, ListView, FormMixin):
    model = Job
    context_object_name = 'jobs'
    form_class = JobForm
    success_url = '/jobs'

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['job_count'] = Job.objects.count()
        return context

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return Job.objects.all()
        else:
            return Job.objects.filter(user=user)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        form = self.get_form()
        return self.form_valid(form)

    def form_valid(self, form):
        # commit=False so that we can add some non-user exposed options
        # commit defaults to True which means it normally saves.
        job_instance = form.save(commit=False)
        job_instance.user = self.request.user
        job_instance.type = 'scan'
        job_instance.save()
        messages.success(self.request,
                         'Successfully Created '
                         'Job ID {} '.format(job_instance.id))
        # return object
        return HttpResponseRedirect('/jobs/')


class SpeedTestResultsListView(LoginRequiredMixin, ListView, FormMixin):
    model = SpeedTestResult
    context_object_name = 'speedtests'
    form_class = JobForm
    success_url = '/speedtests'

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return SpeedTestResult.objects.all()
        else:
            return SpeedTestResult.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super(SpeedTestResultsListView,
                        self).get_context_data(**kwargs)
        context['results'] = dict()
        # TODO: This is probably be ready to cleaned up now.
        # Needs to be tested
        # This is a little goofy, we need to deserialize SpeedTest.results
        # so it can be passed to template as dict

        for i in self.object_list:
            data = json.loads(i.results)
            i.results = data

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        form = self.get_form()
        return self.form_valid(form)

    def form_valid(self, form):
        job = Job(user=self.request.user,
                  type='speedtest',
                  destination='speedtest.net',
                  ports='all')
        job.save()
        messages.success(self.request,
                         'Successfully Created Job ID {} '.format(job.id))

        return HttpResponseRedirect('/speedtests/')


class JobDetailView(LoginRequiredMixin, DetailView):
    template_name = 'discover/job_detail.html'
    model = Job
    queryset = Job.objects.all()

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)

        if self.object.type == 'scan':
            # TODO likely a bug here, in the case where a
            # job has not been completed, for now we are only
            # setting adding processed jobs to the JobListView queryset,
            data = json.loads(json.dumps(self.object.results))['scan']
            context['hosts'] = data

        return context

# API VIEWS


class SpeedTestResultViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SpeedTestResultSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return SpeedTestResult.objects.all()
        else:

            return SpeedTestResult.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for working with jobs.
    """
    serializer_class = serializers.JobSerializer
    queryset = Job.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('processed', 'type',)
    permissions_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Return a list of all the gateways for the current user
        """
        user = self.request.user
        return Job.objects.filter(user=user)

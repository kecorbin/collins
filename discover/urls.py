from django.conf.urls import url
from views import JobListView, JobDetailView, SpeedTestResultsListView

urlpatterns = [
               url(r'jobs/$',
                   JobListView.as_view(),
                   name='job_list'),

               url(r'^jobs/(?P<pk>\d+)/',
                   JobDetailView.as_view(
                       template_name='discover/job_detail.html'),
                   name='job-detail'),

               url(r'^speedtests/$',
                   SpeedTestResultsListView.as_view(
                       template_name='discover/speedtests.html'),
                   name='speedtest_list')
               ]

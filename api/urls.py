from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views as restviews
from api.views import JobViewSet, ResultViewSet, EnvironmentViewSet, IntervalScheduleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet, base_name='job-detail')
router.register(r'results', ResultViewSet, base_name='response-detail')
router.register(r'environments', EnvironmentViewSet, base_name='environment-detail')
router.register(r'intervals', IntervalScheduleViewSet, base_name='intervalschedule-detai')
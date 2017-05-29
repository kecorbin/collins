from act.views import (JobViewSet,
                       JobResultViewSet,
                       ResultViewSet,
                       EnvironmentViewSet,
                       IntervalScheduleViewSet,
                       SchedulerViewSet,
                       PluginViewSet)

from discover.urls import router as discover_router
from connect.urls import router as connect_router
from rest_framework_nested.routers import NestedSimpleRouter

from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'jobs',
                JobViewSet,
                base_name='job-detail')

router.register(r'results',
                ResultViewSet,
                base_name='result-detail')

router.register(r'environments',
                EnvironmentViewSet,
                base_name='environment-detail')

router.register(r'intervals',
                IntervalScheduleViewSet,
                base_name='intervalschedule-detail')

job_results_router = NestedSimpleRouter(router,
                                        r'jobs',
                                        lookup='job')

job_results_router.register(r'results',
                            JobResultViewSet,
                            base_name='job-results')

router.register(r'schedulers',
                SchedulerViewSet,
                base_name='scheduler-detail')

router.register(r'plugins',
                PluginViewSet,
                base_name='plugins')


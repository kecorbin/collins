from api.views import (JobViewSet,
                       JobResultViewSet,
                       ResultViewSet,
                       EnvironmentViewSet,
                       IntervalScheduleViewSet)


from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

router = routers.DefaultRouter()

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

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


class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """
    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)

router = DefaultRouter(trailing_slash=True)

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


router.extend(discover_router)
router.extend(connect_router)
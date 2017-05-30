from act.views import (JobViewSet,
                       JobResultViewSet,
                       ResultViewSet,
                       EnvironmentViewSet,
                       IntervalScheduleViewSet,
                       SchedulerViewSet,
                       PluginViewSet)


from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'jobs',
                JobViewSet,
                base_name='job')

router.register(r'results',
                ResultViewSet,
                base_name='result-detail')

router.register(r'environments',
                EnvironmentViewSet,
                base_name='environment-detail')

router.register(r'intervals',
                IntervalScheduleViewSet,
                base_name='intervalschedule-detail')


router.register(r'schedulers',
                SchedulerViewSet,
                base_name='scheduler-detail')

router.register(r'plugins',
                PluginViewSet,
                base_name='plugins')


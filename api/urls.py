from api.views import (JobViewSet,
                       JobResultViewSet,
                       ResultViewSet,
                       EnvironmentViewSet,
                       IntervalScheduleViewSet,
                       SchedulerViewSet,
                       PluginViewSet)
from discover.views import JobViewSet, SpeedTestResultViewSet
from connect.views import (CloudServerViewSet, CreateTunnelViewSet,
                           TunnelListViewSet, GatewayViewSet,
                           GatewayUpdateView, ProxyPortViewSet)

from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

router = routers.DefaultRouter(trailing_slash=False)

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

router.register(r'gateway',
                GatewayViewSet,
                base_name='gateway-detail')
router.register(r'tunnels',
                TunnelListViewSet,
                base_name='tunnel-detail')

router.register(r'tunnel',
                TunnelListViewSet,
                base_name='tunnel-detail')
router.register(r'createtunnel',
                CreateTunnelViewSet,
                base_name='create-tunnel')
router.register(r'cloudserver',
                CloudServerViewSet)
router.register(r'jobs',
                JobViewSet,
                base_name='jobs-detail')
router.register(r'scans',
                JobViewSet,
                base_name='jobs-detail')

router.register(r'speedtests',
                SpeedTestResultViewSet,
                base_name='speedtests')
router.register(r'proxyport',
                ProxyPortViewSet,
                base_name='proxyport')
router.register(r'plugins',
                PluginViewSet,
                base_name='plugins')

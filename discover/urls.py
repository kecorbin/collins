from rest_framework import routers
from discover.views import ScanViewSet, SpeedTestViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'scans',
                ScanViewSet,
                base_name='scans-list')

router.register(r'speedtests',
                SpeedTestViewSet,
                base_name='speedtests-list')

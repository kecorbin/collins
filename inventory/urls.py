from rest_framework import routers
from connect.views import GatewayViewSet
from views import SystemViewSet, DeviceViewSet

router = routers.DefaultRouter(trailing_slash=True)


router.register(r'gateways',
                GatewayViewSet,
                base_name='gateway-detail')

# router.register(r'systems',
#                 SystemViewSet,
#                 base_name='systems-list')
#
# router.register(r'devices',
#                 DeviceViewSet,
#                 base_name='devices-list')

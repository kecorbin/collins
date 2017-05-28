from rest_framework import routers
from views import SystemViewSet, DeviceViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'systems',
                SystemViewSet,
                base_name='systems-list')

router.register(r'devices',
                DeviceViewSet,
                base_name='devices-list')

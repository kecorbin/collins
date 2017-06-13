from rest_framework import routers
from views import GatewayViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'gateways',
                GatewayViewSet,
                base_name='gateway-detail')

from rest_framework import routers
from views import GatewayViewSet, TunnelListViewSet, CreateTunnelViewSet, CloudServerViewSet, ProxyPortViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'gateway',
                GatewayViewSet,
                base_name='gateway-detail')
router.register(r'gateways',
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
router.register(r'proxyport',
                ProxyPortViewSet,
                base_name='proxyport')

from django.conf.urls import include, url
from rest_framework.authtoken import views as restviews
from .views import (
    DashboardView,
    GatewayListView,
    TunnelListView,
    ConsoleTunnel,
)

urlpatterns = [
    # API URLS
    url(r'^grappelli/',
        include('grappelli.urls')),
    url(r'^api/v1/auth/', restviews.obtain_auth_token),

    # UI URLS
    url(r'^gateways/$',
        GatewayListView.as_view(),
        name='gateway-list'),
    url(r'^tunnels/$',
        TunnelListView.as_view(),
        name='tunnel-list'),
    url(r'^console/',
        ConsoleTunnel.as_view(),
        name='console'),
    url(r'^$',
        DashboardView.as_view(),
        name='dashboard'),
]

"""collins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework.authtoken import views as restviews
from discover.urls import router as discover_router
from connect.urls import router as connect_router
from act.urls import router as act_router
from inventory.urls import router as inventory_router
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
router.extend(act_router)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', restviews.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/act/', include(act_router.urls)),
    url(r'^api/v1/discover/', include(discover_router.urls)),
    url(r'^api/v1/connect/', include(connect_router.urls)),
    url(r'^api/v1/inventory/', include(inventory_router.urls))
]

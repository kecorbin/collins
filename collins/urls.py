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
from rest_framework_swagger.views import get_swagger_view
from api.urls import ApiRootRouter

swagger_view = get_swagger_view(title="""

Welcome to the interative api documentation
\n
Have a look around...

""")

router = ApiRootRouter(trailing_slash=True)
router.extend(connect_router)
router.extend(discover_router)
router.extend(inventory_router)
router.extend(act_router)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', swagger_view),
    # Login API
    url(r'^api/v1/auth/', restviews.obtain_auth_token),
    # Login Form
    url(r'^api/v1/login/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # Generate model views from api root e.g /jobs/
    url(r'^api/v1/', include(router.urls)),

    # API Groups/Hierarchy e.g /act/jobs/
    url(r'^api/v1/act/', include(act_router.urls)),
    url(r'^api/v1/discover/', include(discover_router.urls)),
    url(r'^api/v1/connect/', include(connect_router.urls)),
    url(r'^api/v1/inventory/', include(inventory_router.urls))
]

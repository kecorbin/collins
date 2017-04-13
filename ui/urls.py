from django.conf.urls import url
from views import serve_static
urlpatterns = [
               url(r'^jobs/',
                   serve_static,
                   name='job_list'),

               ]

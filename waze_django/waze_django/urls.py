from django.conf.urls import patterns, include, url
from waze_django.views import WazeEndpointHandler

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waze_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'waze-django', WazeEndpointHandler.as_view(), name='waze_django_endpoint'),
)

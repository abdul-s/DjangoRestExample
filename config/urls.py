from django.conf.urls import include, url
from django.contrib import admin
from project import rest_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('project.rest_api.urls')),
]

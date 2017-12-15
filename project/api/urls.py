from django.conf.urls import url, include
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
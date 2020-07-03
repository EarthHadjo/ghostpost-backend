from .views import PostViewSet
from rest_framework import routers
from django.conf.urls import include, url

router = routers.DefaultRouter()

router.register(r'post', PostViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('api/', include(router.urls))
]
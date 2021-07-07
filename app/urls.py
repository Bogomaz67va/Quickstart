from django.urls import path, include
from rest_framework import routers
from app.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(f'users', UserViewSet)
router.register(f'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
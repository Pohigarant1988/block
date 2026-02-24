from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .models import Cats
from .views import PostViewSet, CatsViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')
router.register(r'cats', CatsViewSet, basename='cats')
urlpatterns = [
    path('', include(router.urls)),
]

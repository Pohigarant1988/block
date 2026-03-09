from django.urls import path, include
from rest_framework.routers import DefaultRouter



from .views import PostViewSet, CategoryViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')
router.register(r'cats', CategoryViewSet, basename='cats')
urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import urlpatterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product import views


router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)

app_name = 'product'

urlpatterns = [
  path('', include(router.urls))
]















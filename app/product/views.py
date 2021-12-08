from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

from core.models import Category, Product

from product import serializers


class CategoryViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin):
  """Categories viewset"""
  serializer_class = serializers.CategorySerializer
  queryset = Category.objects.all()
  lookup_field = 'slug'

  def get_queryset(self):
    """Retrieve the categories"""
    return self.queryset

class ProductViewSet(viewsets.ModelViewSet):
  """Manage products in the database"""
  serializer_class = serializers.ProductSerializer
  queryset = Product.objects.all()
  lookup_field = 'slug'

  def get_queryset(self):
    """Retrieve the products"""
    return self.queryset

  











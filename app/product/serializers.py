from rest_framework import serializers

from core.models import Category, Product


class CategorySerializer(serializers.HyperlinkedModelSerializer):
  """Serializer for category objects"""

  class Meta:
    model = Category
    fields = ('id', 'name', 'slug', 'description', 'image')
    lookup_field = 'slug'
    read_only_fields = ('id', 'slug')
    

class ProductSerializer(serializers.HyperlinkedModelSerializer):
  """Serializer a product"""

  class Meta:
    model = Product
    fields = (
        'id',
        'name',
        'description',
        'category',
        'price',
        'image',
        'stock',
        'update'
    )
    lookup_field = 'slug'
    read_only_fields = ('id', 'slug')












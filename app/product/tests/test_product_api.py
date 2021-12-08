import tempfile
import os

from PIL import Image

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Product, Category

from product.serializers import ProductSerializer


PRODUCTS_URL = reverse('product:product-list')


def image_upload_url(product_slug):
  """Return URL for product image upload"""
  return reverse('product:product-upload-image', args=[product_slug])


def detail_url(product_slug):
  """Return product detail URL"""
  return reverse('product:product-detail', args=[product_slug])


def sample_category(name='Apple'):
  """Create and return a sample category"""
  return Category.objects.get_or_create(name=name)


def sample_product(**params):
  """Create and return a sample product"""
  defaults = {
    'name': 'Iphone',
  }
  defaults.update(params)
  return Product.objects.create(**defaults)


class PublicProductApiTests(TestCase):
  """Test unauthenticated product API access"""

  def setUp(self):
    self.client = APIClient()


class PrivateProductApiTests(TestCase):
  """Test unauthenticated product API access"""

  def setUp(self):
    self.client = APIClient()

  def test_retrieve_products(self):
    """Test retrieving a list of products"""
    sample_product()
    sample_product()
    res = self.client.get(PRODUCTS_URL)

    products = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(products)

    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)
















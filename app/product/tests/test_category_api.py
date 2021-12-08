from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Category

from product.serializers import CategorySerializer


CATEGORIES_URL = reverse('product:category-list')



class PrivateCategoryApiTests(TestCase):
  """Test the private categories"""

  def setUp(self):
    self.client = APIClient()

  def test_retrieve_category_list(self):
    """Test retrieving a list of categories"""
    Category.objects.get_or_create(name='Apple')
    Category.objects.get_or_create(name='Samsung')

    res = self.client.get(CATEGORIES_URL)

    categories = Category.objects.all().order_by('-name')
    serializer = CategorySerializer(categories)

    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)

  # def test_create_category_successful(self):
  #   """Test create a new category"""
  #   payload = {'name': 'Apple'}
  #   self.client.post(CATEGORIES_URL, payload)
  #   exists = Category.objects.filter(
  #     name=payload['name']
  #   ).exists()
  #   self.assertTrue(exists)

  # def test_create_category_invalid(self):
  #   """Test creating invalid category fails"""
  #   payload = {'name': ''}
  #   res = self.client.post(CATEGORIES_URL, payload)
  #   self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

  









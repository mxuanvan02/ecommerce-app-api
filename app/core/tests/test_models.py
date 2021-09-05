from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
  
  def test_create_user_with_email_successful(self):
    """Test creating a new user with an email successful"""
    email = 'testmail@abc.com'
    password = 'testpassword'
    user = get_user_model().objects.create_user(
      email=email,
      password=password,
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalized(self):
    """Test the email for a new user is normalized"""
    email = 'testmail@ABC.COM'
    user = get_user_model().objects.create_user(email=email, password='abc123')

    self.assertEqual(user.email, email.lower())

  def test_new_user_invalid_email(self):
    """Test creating user with no email raises error"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, 'abc123')

  def test_create_new_superuser(self):
    """Tet creating a new superuser"""
    user = get_user_model().objects.create_superuser(
      'abc@gm.com',
      'abbb'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)






















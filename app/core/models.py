from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin
from django.conf import settings


# def product_image_file_path(instance, filename):
#   """Generate file path for new product image"""
#   ext = filename.split('.')[-1]
#   filename = f''



class UserManager(BaseUserManager):

  def create_user(self, email, password=None, **extra_fields):
    """Creates and saves a new user"""
    if not email:
      raise ValueError('User must have an email address')
    user = self.model(email=self.normalize_email(email), **extra_fields)
    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self, email, password):
    """Creates and saves a new superuser"""
    user = self.create_user(email=email, password=password)
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)

    return user


class User(AbstractBaseUser, PermissionsMixin):
  """Custom user model that suppors using email instead of username"""
  email         = models.EmailField(max_length=255, unique=True)
  name          = models.CharField(max_length=255)
  is_active     = models.BooleanField(default=True)
  is_staff      = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'


class Category(models.Model):
  """Category for product"""
  name          = models.CharField(max_length=255, unique=True)
  slug          = models.SlugField(max_length=255, unique=True)
  description   = models.TextField(blank=True)
  image         = models.ImageField(upload_to='category', blank=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.slug}/'



class Product(models.Model):
  """Product object"""
  name          = models.CharField(max_length=255, unique=True)
  slug          = models.SlugField(max_length=255, unique=True)
  description   = models.TextField(blank=True)
  category      = models.ForeignKey(Category, on_delete=models.CASCADE)
  price         = models.DecimalField(max_digits=10, decimal_places=2)
  image         = models.ImageField(upload_to='product', blank=True)
  stock         = models.IntegerField()
  available     = models.BooleanField(default=True)
  created       = models.DateTimeField(auto_now_add=True)
  update        = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'product'
    verbose_name_plural = 'products'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.category.slug}/{self.slug}/'














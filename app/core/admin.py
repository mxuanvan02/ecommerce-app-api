from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
  ordering = ['id']
  list_display = ['email', 'name']
  fieldsets = (
    (None, {'fields': ('email', 'password', )}),
    (_('Personal Info'), {'fields': ('name', )}),
    (_('Permission'), {'fields': ('is_active', 'is_superuser', )}),
    (_('Important dates'), {'fields': ('last_login', )}),
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'password1', 'password2'),
    }),
  )


class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name',)}



admin.site.register(models.User, UserAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)



















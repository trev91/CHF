from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from polymorphic.models import PolymorphicModel

# Define models here

class User(AbstractUser):
  address1 = models.TextField(null=True, blank=True)
  address2 = models.TextField(null=True, blank=True)
  birth = models.DateTimeField(null=True, blank=True)
  phone_number = models.TextField(null=True, blank=True)
  
admin.site.register(User)
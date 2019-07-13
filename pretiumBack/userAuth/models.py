from django.db import models
from django.contrib.auth.models import AbstractUser

from . import helper


class User(AbstractUser):
    """Extend functionality of user"""
    hash_id = models.CharField(max_length=32, default=helper.create_hash(), unique=True)
    fullname = models.CharField(max_length=50, unique=False)
    imageURL = models.CharField(max_length=150, unique=False, default='')

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        error_messages={
            'add': 'The permission you are trying to add already exists for the user.',
            'remove': 'The permission you are trying to remove does not exist for the user.',
        },
    )
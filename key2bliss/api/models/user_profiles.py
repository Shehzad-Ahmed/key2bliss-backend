"""Contains ORM model for user profiles.
"""
from django.db import models

from key2bliss.backends import UserMediaStorage


class UserProfiles(models.Model):
    """ORM class for user profile.
    """

    user = models.OneToOneField("users", primary_key=True, on_delete=models.CASCADE)

    phone_number = models.TextField(null=True, default="", blank=True)

    age = models.IntegerField(null=True)

    photo = models.ImageField(storage=UserMediaStorage(), null=True)

"""Contains ORM models for users.
"""
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from key2bliss.api.managers import CustomUserManager
from key2bliss.api.models import Base


class Users(AbstractUser, Base):
    """ORM model class for users
    """

    email = models.EmailField(max_length=150,
                              unique=True,
                              help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                              validators=[EmailValidator],
                              error_messages={
                                  'unique': _("This email address is already taken."),
                              }, )

    REQUIRED_FIELDS = []

    date_joined = None

    objects = CustomUserManager()

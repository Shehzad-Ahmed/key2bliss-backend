"""Contains ORM models for User Queries.
"""
from django.db import models
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

from key2bliss.api.models import Base


class ReportedProblems(Base):
    """ORM model class for Reported problems.
    """

    deleted = None

    full_name = models.TextField()

    email = models.EmailField(
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[EmailValidator],
        error_messages={
            'unique': _("This email address is already taken."),
        },
    )

    message = models.TextField()

    resolved = models.BooleanField(default=False)

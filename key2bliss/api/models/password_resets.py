"""Contains ORM models for User Resetting Password.
"""
from django.db import models

from key2bliss.api.models import Base


class PasswordResets(Base):
    """ORM model for password Resets.
    """
    user = models.ForeignKey("Users", on_delete=models.CASCADE, related_name="password_resets")

    performed = models.BooleanField(default=False)

    def send_email(self):
        """Sends email to user containing password reset Token.
        """
        if self.is_valid():
            self.user.email_user(subject="Reset Password", message=f"token: {str(self.id)}")

    def is_valid(self):
        """Whether the password Reset entry is valid.
        """
        return not (self.performed or self.deleted or self.is_expired())

    def is_expired(self):
        """Checks whether the entry is expired.
        """
        return False

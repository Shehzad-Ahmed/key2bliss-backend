"""Manager Classes for Users.
"""
from django.contrib.auth.models import UserManager
from django.db.models import Q


class CustomUserManager(UserManager):
    """Custom Manager class.
    """

    def get_by_natural_key(self, username_or_email):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username_or_email}) | Q(**{self.model.EMAIL_FIELD: username_or_email})
        )

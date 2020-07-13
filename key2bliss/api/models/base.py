"""Contains Abstract Base ORM models.
"""
from uuid import uuid4

from django.db import models


class Base(models.Model):
    """Abstract Base ORM model.
    """

    id = models.UUIDField(primary_key=True, default=uuid4)

    created_on = models.DateField(auto_now_add=True)

    deleted = models.BooleanField(default=False)

    class Meta:
        """Meta Class
        """

        abstract = True

    def delete(self, using=None, keep_parents=False, hard=False):
        """Over-riding to support soft delete.

        :param using: See Parent Class function for details.
        :param keep_parents: See Parent Class function for details.
        :param hard: Whether to delete entry from database or to mark as deleted. Defaults to False
        """
        if hard:
            details = super().delete(using, keep_parents)
        else:
            self.delete = True
            self.save()
            details = self
        return details

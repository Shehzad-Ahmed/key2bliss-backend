"""Contains ORM models for Files.
"""
from django.db import models

from key2bliss.api.models import Base

FILE_TYPES = (
    ("video", "Video"),
    ("image", "Image"),
    ("audio", "Audio")
)

class Files(Base):
    """ORM model class for Files
    """

    name = models.TextField()

    type = models.TextField()

    s3_key = models.TextField()

    extension = models.TextField()

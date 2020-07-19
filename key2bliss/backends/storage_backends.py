"""Contains the Storage Backends Classes.
"""

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """Backend class for storing public assets on S3
    """
    location = settings.AWS_PUBLIC_MEDIA_LOCATION

    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    """Backend class for storing private assets on S3
    """
    location = settings.AWS_PRIVATE_MEDIA_LOCATION

    default_acl = 'private'

    file_overwrite = False

    custom_domain = False


class UserMediaStorage(S3Boto3Storage):
    """Backend class for storing private assets on S3
    """
    location = settings.AWS_USER_MEDIA_LOCATION

    default_acl = 'private'

    file_overwrite = False

    custom_domain = False

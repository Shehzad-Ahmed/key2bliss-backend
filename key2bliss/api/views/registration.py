"""API end points for Registration.
"""
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework import viewsets

from key2bliss.api.serializers.users import UserRegistrationSerializer

User = get_user_model()


class UserRegistrationViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """USer Registration API End point.
    """

    serializer_class = UserRegistrationSerializer

    queryset = User.objects.filter(deleted=False, is_active=True)

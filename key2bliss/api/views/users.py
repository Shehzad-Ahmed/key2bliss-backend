"""API End points related to users
"""
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from key2bliss.api.serializers import UserChangePasswordsSerializer

User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Users ViewSet class
    """

    queryset = User.objects.filter(deleted=False, is_active=True)

    permission_classes = (IsAuthenticated,)

    serializer_mapping = {
        "change_password": UserChangePasswordsSerializer
    }

    @action(methods=["post"], detail=False, url_name="change-password")
    def change_password(self, request, *args, **kwargs):
        """API End point for changing users password.

        :param request: The rest framework request object.
        """
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        """Returns serializer according to action,
        """
        return self.serializer_mapping.get(self.action, super().get_serializer_class())

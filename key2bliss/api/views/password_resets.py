"""API endpoints related to User Passwords operations.
"""
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from key2bliss.api.serializers.password_resets import PasswordResetsSerializer


class PasswordsViewSet(viewsets.ViewSet):
    """Password Resets API endpoints.
    """

    @action(methods=["post"], detail=False, url_name="forgot-password")
    def forgot(self, request, *args, **kwargs):
        """API End point for forgetting password.

        :param request: The rest framework request object.
        """
        serializer = PasswordResetsSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class PasswordResetConfirmCustomView(PasswordResetConfirmView):
    """Inheriting to inject custom template.
    """

    template_name = "passwords/password_reset_confirm_custom.html"


class PasswordResetCompleteCustomView(PasswordResetCompleteView):
    """Inheriting to inject custom template.
    """

    template_name = "passwords/password_reset_complete_custom.html"

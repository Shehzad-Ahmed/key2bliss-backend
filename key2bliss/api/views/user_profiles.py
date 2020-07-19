"""API Endpoints for user profiles.
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from key2bliss.api.models import UserProfiles
from key2bliss.api.serializers import UserProfilesSerializer
from key2bliss.api.serializers.user_profiles import UserProfilePhotoSerializer


class UserProfilesViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.UpdateModelMixin
):
    """View Set Class for User profiles.
    """

    serializer_class = UserProfilesSerializer

    queryset = UserProfiles.objects.all()

    permission_classes = (IsAuthenticated,)

    lookup_field = "user"

    def get_object(self):
        """Over-riding to supply logged in user for look up field.
        """

        try:
            self.request.user.userprofiles
        except UserProfiles.DoesNotExist:
            serializer = self.get_serializer(data={})
            serializer.is_valid(raise_exception=True)
            serializer.save()
        self.kwargs["user"] = self.request.user
        return super().get_object()

    def list(self, request, *args, **kwargs):
        """Over-riding to create user profile exists for requesting user

        :param request: The rest framework.
        """
        return super().retrieve(request, *args, **kwargs)

    @action(methods=["put", "patch"], detail=False, url_path="upload-photo", url_name="upload-profile-photo")
    def upload_photo(self, request, *args, **kwargs):
        """API-Endpoint for uploading a profile picture.

        :param request: The rest framework request object.
        """
        self.serializer_class = UserProfilePhotoSerializer
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=["delete"], detail=False, url_path="remove-photo", url_name="remove-profile-photo")
    def remove_photo(self, request, *args, **kwargs):
        """API-Endpoint for removing a profile picture.

        :param request: The rest framework request object.
        """
        instance = self.get_object()
        if instance.photo:
            instance.photo.delete()
            response = Response(
                {"message": "Profile Photo Removed", "success": True}, status=status.HTTP_200_OK
            )
        else:
            response = Response(
                {"message": "Profile Photo not Uploaded", "success": False}, status=status.HTTP_404_NOT_FOUND
            )
        return response

"""Contains Serializer for User Profiles.
"""
from rest_framework import serializers

from key2bliss.api.models import UserProfiles


class UserProfilesSerializer(serializers.ModelSerializer):
    """Model Serializer class for User Profiles
    """

    class Meta:
        """Meta class
        """

        model = UserProfiles

        fields = (
            "user",
            "phone_number",
            "age",
            "photo",
        )

        read_only_fields = (
            "user",
            "photo",
        )

    def create(self, validated_data):
        """Creates the user profile for requesting user

        :param validated_data: The validated data
        """
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

class UserProfilePhotoSerializer(serializers.ModelSerializer):
    """Model serializer class for user profile photo.
    """

    class Meta:
        """Meta Class
        """

        model = UserProfiles

        fields = (
            "photo",
        )

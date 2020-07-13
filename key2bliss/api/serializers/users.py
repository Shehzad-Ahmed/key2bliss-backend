"""Contains serializers for users
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """User serializer
    """

    tokens = serializers.SerializerMethodField()

    class Meta:
        """Meta class
        """
        model = User

        fields = (
            "id",
            "created_on",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "is_active",
            "tokens",
        )

        read_only_fields = (
            "id",
            "created_on",
            "is_active",
            "tokens"
        )

    def get_tokens(self, instance):
        """Returns user JWT tokens

        :param instance: The user instance
        """
        refresh = RefreshToken.for_user(instance)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }

    def create(self, validated_data):
        password = validated_data.pop("password")

        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance

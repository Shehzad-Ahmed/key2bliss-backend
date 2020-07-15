"""Contains serializers for users
"""
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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

    def validate(self, attrs):
        """Over-riding to validate password.

        :param attrs: The attributes to validate
        """
        try:
            password_validation.validate_password(attrs["password"])
        except DjangoValidationError as exc:
            raise ValidationError({"password": exc.messages})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        self._data = {
            "success": True, "tokens": self.get_tokens(instance)
        }
        return instance


class UserChangePasswordsSerializer(serializers.Serializer):
    """Serializer class for changing password.
    """

    old_password = serializers.CharField(required=True)

    new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        """Over-riding to perform custom validations.

        :param attrs: The attributes to validate.
        """
        user = self.context["request"].user
        error_messages = {}
        if not user.check_password(attrs["old_password"]):
            error_messages["old_password"] = "wrong password"
        try:
            password_validation.validate_password(attrs["new_password"])
        except DjangoValidationError as exc:
            error_messages["new_password"] = exc.messages
        if error_messages:
            raise ValidationError(error_messages)
        return super().validate(attrs)

    def create(self, validated_data):
        """Changes the password for user

        :param validated_data: The validated data
        """
        user = self.context["request"].user
        password = validated_data["new_password"]
        user.set_password(password)
        user.save()
        self._data = {
            "success": True, "message": "Password Changed"
        }
        return object

"""Serializers for reported problems.
"""
from rest_framework import serializers

from key2bliss.api.models import ReportedProblems


class ReportedProblemsSerializer(serializers.ModelSerializer):
    """Serializer class for reported problems.
    """

    class Meta:
        """Meta class
        """
        model = ReportedProblems

        fields = "__all__"

        read_only_fields = (
            "id",
            "deleted",
            "created_on",
            "resolved"
        )

"""API Endpoint for reported problems.
"""
from rest_framework import viewsets

from key2bliss.api.models import ReportedProblems
from key2bliss.api.serializers import ReportedProblemsSerializer


class ReportedProblemsViewSet(
    viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin
):
    """View Set class for Reported Problems.
    """

    queryset = ReportedProblems.objects.all()

    serializer_class = ReportedProblemsSerializer

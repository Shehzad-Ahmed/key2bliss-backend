"""Contains Admin Models for Django Admin Panel.
"""
from django.contrib import admin


class ReportedProblemsAdmin(admin.ModelAdmin):
    """Admin Model class for Reported Problems.
    """
    list_display = ("full_name", "email", "created_on", "message", "resolved")

    ordering = ("-created_on",)

    list_per_page = 50

    search_fields = ("full_name", "email", "message")

    list_filter = ("resolved",)

    readonly_fields = ("id", "full_name", "email", "created_on", "message")

    list_editable = ("resolved",)

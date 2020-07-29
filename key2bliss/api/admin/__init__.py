"""contains Registrations for django admin Models.
"""
from django.contrib import admin

from key2bliss.api.admin.models import ReportedProblemsAdmin
from key2bliss.api.models import ReportedProblems

admin.site.register(ReportedProblems, ReportedProblemsAdmin)

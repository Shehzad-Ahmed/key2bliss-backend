"""Contains Serializer for Forgot password.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import _unicode_ci_compare
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.core.validators import EmailValidator
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from key2bliss import settings
from key2bliss.api.models import PasswordResets

User = get_user_model()


class PasswordResetsSerializer(serializers.Serializer):
    """Serializer for Forgot passwords view.
    """

    email = serializers.CharField(max_length=150, validators=[EmailValidator()])

    def create(self, validated_data):
        """Creates the Passwords Reset token and email the corresponding user.

        :param validated_data: The validated data.
        """
        self.reset_password(
            email=validated_data["email"],
            request=self.context["request"],
            email_template_name="passwords/password_reset_email_custom.html"
        )
        self._data = {
            "success": True,
            "message": "If the user exists in our system, then the email has been sent."
        }
        return object

    def reset_password(self, email, domain_override=None,
                       subject_template_name="registration/password_reset_subject.txt",
                       email_template_name="registration/password_reset_email.html",
                       token_generator=default_token_generator,
                       from_email=None, request=None, html_email_template_name=None,
                       extra_email_context=None):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email_field_name = User.get_email_field_name()
        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            user_email = getattr(user, email_field_name)
            context = {
                'email': user_email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if settings.USE_HTTPS_IN_RESET_PASSWORD else 'http',
                'app_name': 'Key2Bliss',
                **(extra_email_context or {}),
            }
            self.send_mail(
                subject_template_name, email_template_name, context, from_email,
                user_email, html_email_template_name=html_email_template_name,
            )

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        email_field_name = User.get_email_field_name()
        active_users = User._default_manager.filter(**{
            '%s__iexact' % email_field_name: email,
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password() and
               _unicode_ci_compare(email, getattr(u, email_field_name))
        )

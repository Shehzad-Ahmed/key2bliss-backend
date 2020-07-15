"""Urls for API app.
"""
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from key2bliss.api import views

router = routers.DefaultRouter()

router.register("signup", views.UserRegistrationViewSet, basename="signup")

router.register("passwords", views.PasswordsViewSet, basename="password")

router.register("user", views.UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("passwords/reset/<uidb64>/<token>/", views.PasswordResetConfirmCustomView.as_view(),
         name='password_reset_confirm'),
    path("passwords/reset/done/", views.PasswordResetCompleteCustomView.as_view(), name='password_reset_complete'),
]

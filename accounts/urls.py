from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView, ProfileView,
    ChangePasswordView, SendPasswordResetEmailView, ResetPasswordView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("password-reset-request/", SendPasswordResetEmailView.as_view(), name="password-reset-request"),
    path("password-reset-confirm/", ResetPasswordView.as_view(), name="password-reset-confirm"),
]

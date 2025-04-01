from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register, login, user_profile, activate_account, request_password_reset, reset_password


urlpatterns = [
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("activate/<str:uidb64>/<str:token>", activate_account, name="activate_account"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile", user_profile, name="profile"),
    path("request-password-reset", request_password_reset, name="request_password_reset"),
    path('reset-password/<str:uidb64>/<str:token>', reset_password, name='reset-password'),
    path('lecturers/', user_profile, name='list-lecturers'),
    path('students/', user_profile, name='list-students'),
    path('registrars/', user_profile, name='list-registrars'),
    
]
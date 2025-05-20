from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import user


urlpatterns = [
    path('register/', user.UserRegistrationView.as_view(), name='user_registration'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/profile/', user.UserAuth.as_view(), name='user_auth'),
    path('user/change-password/', user.ChangePasswordView.as_view(), name='change_password'),
    path('password-reset/', user.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/<int:id>/<str:token>/', user.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

]
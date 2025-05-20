from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    UserSerializer,
    ChangePasswordSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer
)


class UserAuth(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete the authenticated user's account.

    - GET: Retrieve the current user's data.
    - PUT/PATCH: Update the current user's data.
    - DELETE: Delete the current user's account.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Returns the currently authenticated user.
        """
        return self.request.user


class ChangePasswordView(generics.GenericAPIView):
    """
    API endpoint to allow authenticated users to change their password.

    - PUT: Update the user's password.
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Returns the currently authenticated user.
        """
        return self.request.user

    def put(self, request, *args, **kwargs):
        """
        Validates and updates the user's password.
        """
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.object.set_password(serializer.validated_data['new_password'])
        self.object.save()
        return Response({'detail': 'Password updated successfully.'})


class PasswordResetView(generics.GenericAPIView):
    """
    API endpoint to request a password reset email.

    - POST: Sends an email to the user with instructions to reset their password.
    """
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        """
        Validates the email and sends the password reset email.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "An email has been sent with instructions on how to reset your password."},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmView(generics.GenericAPIView):
    """
    API endpoint to confirm the password reset and set a new password.

    - POST: Validates the reset token and updates the password.
    """
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        """
        Validates the token and UID, sets the new password.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response(
            {'detail': 'Password reset successfully.'},
            status=status.HTTP_200_OK
        )

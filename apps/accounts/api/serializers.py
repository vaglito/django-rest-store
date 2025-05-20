from importlib.metadata import requires
from django.contrib.auth.models import Group, User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from rest_framework import serializers

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer used for user registration.
    """
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer used for changing a user's password.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        """
        Validate the new password using Django's password validators
        and check that the old password is correct.
        """
        try:
            validate_password(data['new_password'], self.context['request'].user)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'new_password': list(e.messages)})
        
        if not self.context['request'].user.check_password(data['old_password']):
            raise serializers.ValidationError({'old_password': 'Old password is incorrect.'})
        
        return data


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user data, includes basic fields and groups.
    """
    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for user groups using hyperlinked relationships.
    """
    class Meta:
        model = Group
        fields = ['url', 'name']


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for initiating password reset by email.
    """
    email = serializers.EmailField()
    
    def validate_email(self, value):
        """
        Validate that the email belongs to a registered user.
        """
        self.reset_form = PasswordResetForm(data={'email': value})
        if not self.reset_form.is_valid():
            raise serializers.ValidationError("There is no user registered with this email.")
        return value

    def save(self):
        """
        Send password reset email using Django's built-in PasswordResetForm.
        """
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com'),
            'email_template_name': 'email/password_reset_email.html',
            'subject_template_name': 'email/password_reset_subject.txt',
            'request': request,
        }
        self.reset_form.save(**opts)


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for confirming a password reset using token and user ID.
    """
    id = serializers.IntegerField()
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8, style={'input_type': 'password'})
    new_password_confirm = serializers.CharField(min_length=8, style={'input_type': 'password'})

    def validate(self, attrs):
        """
        Validate that the token is valid, the user exists, and passwords match.
        """
        try:
            self.user = User.objects.get(pk=attrs['id'])
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError({'id': 'Invalid password reset link.'})

        if not default_token_generator.check_token(self.user, attrs['token']):
            raise serializers.ValidationError({'token': 'Invalid or expired token.'})

        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({'new_password': 'Passwords do not match.'})

        return attrs

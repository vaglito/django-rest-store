from django.contrib.auth.models import Group, User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        try:
            validate_password(data['new_password'], self.context['request'].user)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'new_password': list(e.messages)})
        
        if not self.context['request'].user.check_password(data['old_password']):
            raise serializers.ValidationError({'old_password': 'Old password is incorrect.'})
        
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
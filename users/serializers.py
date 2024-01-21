from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import UserConfirmation


class AuthorizeValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RegisterValidateSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email =serializers.EmailField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exist')

    class Meta:
        model = User
        fields = ['username', 'password','email']


class UserConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfirmation
        fields = ['code']

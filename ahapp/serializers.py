from email.policy import default

from wsgiref.validate import validator
from pkg_resources import require
from .models import Problem, Profile as Pro
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers as ser
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate


class RegisterSerializer(ser.ModelSerializer):
    password = ser.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = ser.CharField(
        write_only=True, required=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ser.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user


class LoginSerializer(ser.Serializer):
    username = ser.CharField(required=True)
    password = ser.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise ser.ValidationError(
            {"error": "Unable to login woth provided credentials."}
        )


class ProfileSerializer(ser.ModelSerializer):
    class Meta:
        model = Pro
        fields = ('bojid',)


class ProblemSerializer(ser.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('name', 'link')

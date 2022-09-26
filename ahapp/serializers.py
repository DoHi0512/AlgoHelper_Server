from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
import requests
import json
tierList = [
    "b5",
    "b4",
    "b3",
    "b2",
    "b1",
    "s5",
    "s4",
    "s3",
    "s2",
    "s1",
    "g5",
    "g4",
    "g3",
    "g2",
    "g1",
    "p5",
    "p4",
    "p3",
    "p2",
    "p1",
    "d5",
    "d4",
    "d3",
    "d2",
    "d1",
    "r5",
    "r4",
    "r3",
    "r2",
    "r1",
]

class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    boj_id = serializers.CharField()

    class Meta:
        model = User
        fields = ('name', 'password', 'password2', 'boj_id')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': 'password fields did not match'}
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['name'],
            validated_data['password'],
            boj_id=validated_data['boj_id'],
        )
        user.save()
        res = requests.get(
            f"https://solved.ac/api/v3/user/show?handle={user.boj_id}")
        if res.status_code == 200:
            res = res.json()
            first = res['tier'] - 4
            end = res['tier'] + 1
            if first < 0:
                first = 0
            if end >= len(tierList):
                end = len(tierList) - 1
            newTier = "*" + tierList[first] + \
                ".." + tierList[end]
            response = requests.get("https://solved.ac/api/v3/search/problem",
                                    params={'query': newTier + ' ' + f'!@{user.boj_id}' + ' lang:ko', 'sort': 'random'})
            user.problem = response.text
            user.save()
        token = Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        return 'error'

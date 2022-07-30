from http.client import ResponseNotReady
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.urls import is_valid_path
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from ahapp.serializers import *
from .models import Profile as pro


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        token = serializer.validated_data
        return Response({"token": token.key})


class ProfileView(generics.RetrieveAPIView):
    queryset = Pro.objects.all()
    serializer_class = ProfileSerializer


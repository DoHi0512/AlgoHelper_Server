from ast import Subscript
import re
from tokenize import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from urllib.request import urlopen
from bs4 import BeautifulSoup

from .serializers import LoginSerializer, RegisterSerializer
from .models import *
from rest_framework import viewsets, permissions, generics, status
import datetime


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        temp = ''
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        print(type(token))
        if not isinstance(token, str):
            temp = token.key
        else:
            temp = 'error'
        return Response({'token': temp}, status=status.HTTP_200_OK)


class GetBoj(APIView):
    def get(self, request):
        user = User.objects.get(name=request.GET['name'])
        return Response(data=user.boj_id, status=status.HTTP_200_OK)

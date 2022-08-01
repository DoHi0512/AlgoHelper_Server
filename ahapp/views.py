from http.client import ResponseNotReady
from os import stat
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.urls import is_valid_path
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from ahapp.serializers import *
from .models import Profile as pro
from urllib.request import urlopen
from bs4 import BeautifulSoup


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


@api_view(['GET'])
def ProblemAPI(request):
    html = urlopen(
        "https://solved.ac/search?query=*r1&sort=random&direction=asc&page=1")
    bsObject = BeautifulSoup(html, "html.parser")
    problem = []
    link = []
    for lin in bsObject.find_all('a'):
        temp = str(lin.find_all('span', {'class': '__Latex__'}))
        if temp[1] == '<':
            problem.append(temp[25:-8])
            link.append(lin.get('href'))
    return Response([problem, link])

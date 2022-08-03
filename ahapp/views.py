from http.client import ResponseNotReady
import json
from os import stat
import re
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
        if serializer.is_valid():
            token = serializer.validated_data
            return Response({"token": token.key})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveAPIView):
    queryset = Pro.objects.all()
    serializer_class = ProfileSerializer


@api_view(['POST'])
def ProblemAPI(request):
    html = urlopen(request.data['url'])
    bsObject = BeautifulSoup(html, "html.parser")
    problem = []
    link = []
    imgurl = []
    for lin in bsObject.find_all('a'):
        temp = str(lin.find_all('span', {'class': '__Latex__'}))
        if temp[1] == '<':
            problem.append(temp[25:-8])
            link.append(lin.get('href'))
    for lin in bsObject.find_all('img', {'class': 'css-1vnxcg0'}):
        imgurl.append(lin.get('src'))
    return Response(data={'problem': problem, 'urls': link, 'imgurl': imgurl}, status=status.HTTP_200_OK)


@api_view(['POST'])
def UserSolvedAPI(request):
    html = urlopen("https://www.acmicpc.net/user/" + request.data['username'])

    bsObject = BeautifulSoup(html, "html.parser")
    solved = []
    for pro in bsObject.find('div', {'class': 'problem-list'}):
        if pro.text.strip() != '':
            solved.append(pro.text.strip())
    return Response(data=solved, status=status.HTTP_200_OK)

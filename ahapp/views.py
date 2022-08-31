from ast import Subscript
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


@api_view(['POST'])
def ProblemAPI(request):
    html = urlopen(request.data['url'])
    bsObject = BeautifulSoup(html, "html.parser")
    problem = []
    for lin in bsObject.find_all('a'):
        obj = {}
        temp = str(lin.find_all('span', {'class': '__Latex__'}))
        if temp[1] == '<' and len(problem) < 7:
            obj['problem'] = temp[25:-8]
            obj['url'] = lin.get('href')
            problem.append(obj)
    i = 0
    for link in bsObject.find_all('img', {'class': 'css-1vnxcg0'}):
        if i == 7 : break
        problem[i]['img'] = link.get('src')
        i += 1
    return Response(data=problem, status=status.HTTP_200_OK)


@api_view(['POST'])
def GetBoj(request):
    name = request.data['name']
    user = User.objects.get(name=name)
    print(user.boj_id)
    return Response(data=user.boj_id, status=status.HTTP_200_OK)

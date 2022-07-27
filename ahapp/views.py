from http.client import ResponseNotReady
import re
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.urls import is_valid_path
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from ahapp.serializers import UserSerializer
from .models import *
import json
# Create your views here.


# @api_view(['GET'])
# def HelloAPI(request):
#     return Response("Hello world")


# @api_view(['GET', 'POST'])
# def booksAPI(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def bookAPI(request, bid):
#     book = get_object_or_404(Book, bid=bid)
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def allUserAPI(request):
    user = Users.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def userInfoAPI(request, id):
    user = get_object_or_404(Users, id=id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def registerAPI(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginCheckAPI(request):
    data = json.loads(request)
    check = get_object_or_404(Users, userName=data[userName], passwd=data[passwd])
    if check != '404':
        return Response(True)
    return Response(status=status.HTTP_400_BAD_REQUEST)

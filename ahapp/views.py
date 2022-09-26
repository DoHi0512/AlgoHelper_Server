from email.policy import HTTP
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import LoginSerializer, RegisterSerializer
from .models import *
from rest_framework import generics, status
import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler
import time
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


def job():
    users = User.objects.all()
    for user in users:
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
            print(f'{user.name} is changed')
        time.sleep(4)


def main():
    sched = BackgroundScheduler()
    sched.add_job(job, 'cron', day_of_week = 'mon' , hour = 9, id='test')
    sched.start()


@api_view(['GET'])
def ProblemAPI(request):
    name = request.GET['username']
    pro = User.objects.get(name=name)
    pro = json.loads(pro.problem)
    return Response(data=pro, status=status.HTTP_200_OK)


# @api_view(['PUT'])
# def ModifyAPI(request):
#     name = request.data['username']
#     user = User.objects.get(name = name)
#     user.delete()
#     return Response(status=status.HTTP_200_OK)

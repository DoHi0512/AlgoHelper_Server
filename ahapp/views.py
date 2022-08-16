import imp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from rest_framework import viewsets, permissions, generics, status


@api_view(['POST'])
def Register(request):
    user = UserManager()
    username = request.data['username']
    boj_id = request.data['boj_id']
    password = request.data['password']
    user.create_user(username, boj_id, password)

    return Response(data = user,status=status.HTTP_200_OK)

    # @api_view(['POST'])
    # def ProblemAPI(request):
    #     html = urlopen(request.data['url'])
    #     bsObject = BeautifulSoup(html, "html.parser")
    #     problem = {'problem': [], 'url': [], 'imgs': []}
    #     for lin in bsObject.find_all('a'):
    #         temp = str(lin.find_all('span', {'class': '__Latex__'}))
    #         if temp[1] == '<' and len(problem['problem']) < 7:
    #             problem['problem'].append(temp[25:-8])
    #             problem['url'].append(lin.get('href'))
    #         for lin in bsObject.find_all('img', {'class': 'css-1vnxcg0'}):
    #             if len(problem['imgs']) < 7:
    #                 problem['imgs'].append(lin.get('src'))

    #     return Response(data={'problem': problem}, status=status.HTTP_200_OK)

    # @api_view(['POST'])
    # def UserSolvedAPI(request):
    #     html = urlopen("https://www.acmicpc.net/user/" + request.data['username'])
    #     bsObject = BeautifulSoup(html, "html.parser")
    #     solved = []
    #     for pro in bsObject.find('div', {'class': 'problem-list'}):
    #         if pro.text.strip() != '':
    #             solved.append(pro.text.strip())
    #     return Response(data=solved, status=status.HTTP_200_OK)

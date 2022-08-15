from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework import generics  # generics class-based view 사용할 계획
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from .serializers import *
from .models import *


@permission_classes([AllowAny])
class Registration(generics.GenericAPIView):
    serializer_class = CustomRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({'message': 'Request Body Error'}, status=status.HTTP_409_CONFLICT)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(request)
        return Response({'user': UserSerializer(user, context=self.get_serializer_context()).data},
                        status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
class Login(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user['username'] == "None":
            return Response({"message": "fail"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data, 
                "token": user['token']
            }
        )
        
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

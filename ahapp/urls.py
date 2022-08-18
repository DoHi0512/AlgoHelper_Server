from xml.etree.ElementInclude import include
from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('problem/', ProblemAPI),
    path('solved/', UserSolvedAPI),
    path('getboj/', GetBoj),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view())
]

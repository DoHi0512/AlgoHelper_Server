from xml.etree.ElementInclude import include
from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('getboj/', GetBoj.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('problem/',ProblemAPI)
]

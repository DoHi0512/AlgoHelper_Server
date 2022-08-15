from xml.etree.ElementInclude import include
from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('problem/', ProblemAPI),
    # path('solved/', UserSolvedAPI),
    # path('api-auth/', include('rest_framework.urls')),
    path('login/', Login.as_view()),
    path('reg/', Registration.as_view())
]

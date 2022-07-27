from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('dohi/userInfo/<int:id>/', userInfoAPI),
    path('dohi/register/', registerAPI),
    path('dohi/allUser/', allUserAPI),
    path('dohi/loginCheck/', loginCheckAPI),
]

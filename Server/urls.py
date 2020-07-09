from django.urls import path
from Server.views import *

urlpatterns = [
    path('user/register', UserRegister.as_view()),
    path('user/login', UserLogin.as_view()),

    path('order/add', OrderAdd.as_view()),
    path('order/agree', OrderAgree.as_view()),
    path('order', GetOrder.as_view()),
]

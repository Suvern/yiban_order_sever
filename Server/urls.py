from django.urls import path
from Server.views.user_views import *
from Server.views.order_views import *
from Server.views.test_views import *

urlpatterns = [
    path('user/register', UserRegister.as_view()),
    path('user/login', UserLogin.as_view()),

    path('order/add', OrderAdd.as_view()),
    path('order/agree', OrderAgree.as_view()),
    path('order', GetOrder.as_view()),

    path('mail', MailSend.as_view())
]

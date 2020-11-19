from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from Server.models.response import JsonResponse
from Server.serializers.serializers import *
from django.core import signing
from django.contrib.auth.hashers import make_password, check_password


# 用户登录
class UserLogin(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data

        username = data['username']
        password = data['password']

        if username is None or password is None:
            return JsonResponse(1, '参数缺失')

        try:
            user_query = User.objects.get(username=username)
            if user_query is None:
                return JsonResponse(1, '用户不存在')
        except:
            return JsonResponse(1, '用户不存在')

        if check_password(password, user_query.password):
            # 存储并返回token
            token = signing.dumps(data['username'])
            Token.objects.update_or_create(username=username, defaults={'token': token})
            return JsonResponse(0, '登录成功', data={'token': token, 'user': UserSerializer(user_query, many=False).data})
        else:
            return JsonResponse(1, '密码错误')


# 用户注册
class UserRegister(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        # 加密
        if (data['username'] is not None) and (data['password'] is not None):
            data['password'] = make_password(data['password'], None, 'pbkdf2_sha256')
            print(data['password'])

        if User.objects.filter(username=data['username']).exists():
            return JsonResponse(1, '用户名已存在')

        data['admin_type'] = '普通用户'
        user = UserSerializer(data=data)

        if user.is_valid():
            user.save()
            user_query = User.objects.get(username=data['username'])
            # 存储并返回token
            token = signing.dumps(data['phone'])
            Token.objects.update_or_create(username=data['username'], defaults={'token': token})
            return JsonResponse(0, '注册成功', data={'token': token, 'user': UserSerializer(user_query, many=False).data})
        else:
            return JsonResponse(1, '参数错误')


# 验证token
def checkToken(token) -> [bool, Response, User]:
    if token is None or len(token) == 0:
        return [False, JsonResponse(1, 'token缺失'), None]
    try:
        token_query = Token.objects.get(token=token)
        user_query = User.objects.get(username=token_query.username)
        if user_query is not None:
            return [True, None, user_query]
    except:
        return [False, JsonResponse(1, 'token失效'), None]


# 判断是否管理员
def checkAdmin(user_query) -> bool:
    return user_query.admin_type != '普通用户'

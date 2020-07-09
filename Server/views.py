from rest_framework.response import Response
from rest_framework.views import APIView
from .response import JsonResponse
from .serializers import *
from django.core import signing
from django.contrib.auth.hashers import make_password, check_password


# 用户登录
class UserLogin(APIView):
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


# 提交预约
class OrderAdd(APIView):
    def post(self, request):
        token = request.META.get("HTTP_TOKEN")
        [flag, response, user_query] = checkToken(token)
        if not flag:
            return response

        data = request.data
        order = OrderSerializer(data=data)

        if order.is_valid():
            order.save(person=user_query)
            return JsonResponse(0, '预约成功')
        else:
            return JsonResponse(1, '参数错误')


# 审核预约
class OrderAgree(APIView):
    def post(self, request):
        token = request.META.get("HTTP_TOKEN")
        [flag, response, user_query] = checkToken(token)
        if not flag:
            return response

        data = request.data
        order_id = data['order_id']
        agreed = data['agreed']
        reason = data['reason']

        if order_id is None or agreed is None or reason is None:
            return JsonResponse(1, '参数错误')

        order_query = Order.objects.get(id=order_id)
        if order_query is None:
            return JsonResponse(1, '预约不存在')

        if agreed:
            order_query.state = '审核通过',
        else:
            order_query.state = '已拒绝'
            order_query.reason = reason

        order_query.save()
        return JsonResponse(0, '审核成功')


# 根据名字、手机号获取预约(普通用户只查询自己的预约，管理员可查询所有预约)
class GetOrder(APIView):
    def get(self, request):
        token = request.META.get("HTTP_TOKEN")
        [flag, response, user_query] = checkToken(token)
        if not flag:
            return response

        query_name = request.GET.get('name')
        query_phone = request.GET.get('phone')

        if checkAdmin(user_query):
            query_set = Order.objects.all()
            if query_name is not None:
                query_set.filter(person_name=query_name)
            if query_phone is not None:
                query_set.filter(person_phone=query_phone)
        else:
            query_set = Order.objects.filter(person__username=user_query.username)

        return JsonResponse(0, '获取成功', OrderSerializer(query_set, many=True).data)


# 验证token
def checkToken(token) -> [bool, Response, User]:
    if token is None or len(token) is 0:
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
    ## 牛b
    return user_query.admin_type != '普通用户'

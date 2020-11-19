from django.db import transaction
from rest_framework.views import APIView
from Server.models.response import JsonResponse
from Server.serializers.serializers import *
from Server.utils.email_utils.email_util import sendNewOrderEmail, sendOrderOrderedEmail
from Server.views.user_views import checkToken, checkAdmin


# 提交预约
class OrderAdd(APIView):
    @transaction.atomic
    def post(self, request):
        token = request.META.get("HTTP_TOKEN")
        [flag, response, user_query] = checkToken(token)
        if not flag:
            return response

        data = request.data
        order = OrderSerializer(data=data)

        if order.is_valid():
            o = order.save(person=user_query)
            print(order.data)

            # 发邮件
            sendNewOrderEmail(o)
            sendOrderOrderedEmail(o)
            return JsonResponse(0, '预约成功')
        else:
            return JsonResponse(1, '参数错误')


# 审核预约
class OrderAgree(APIView):
    @transaction.atomic
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

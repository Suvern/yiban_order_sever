from rest_framework.views import APIView

from Server.models.models import Order
from Server.models.response import JsonResponse
from Server.utils.email_utils.email_util import sendNewOrderEmail, sendOrderAcceptEmail, sendOrderOrderedEmail


class MailSend(APIView):
    def get(self, request):
        order = Order.objects.last()
        print(sendNewOrderEmail(order))
        print(sendOrderOrderedEmail(order))
        print(sendOrderAcceptEmail(order))
        return JsonResponse(msg='流批')

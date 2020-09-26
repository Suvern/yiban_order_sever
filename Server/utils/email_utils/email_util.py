from django.core.mail import EmailMultiAlternatives
from django import template
from django.template import Context

from Server.models.models import Order
from Server.utils.email_utils.email_data import *

fromEmail = 'flyingstudio@yeah.net'


def sendNewOrderEmail(order: Order) -> bool:
    return sendEmail('【易班大厅预约】新增预约', order, newOrderEmailTemplate)


def sendOrderOrderedEmail(order: Order) -> bool:
    return sendEmail('【易班大厅预约】预约成功', order, orderOrderedTemplate, [getQQEmailFromOrder(order)])


def sendOrderAcceptEmail(order: Order) -> bool:
    return sendEmail('【易班大厅预约】审核通过', order, orderAcceptTemplate, [getQQEmailFromOrder(order)])


def sendOrderRejectedEmail(order: Order) -> bool:
    return sendEmail('【易班大厅预约】审核结果', order, orderRejectedTemplate, [getQQEmailFromOrder(order)])


def getQQEmailFromOrder(order: Order) -> str:
    return f'{order.person.qq}@qq.com'


def sendEmail(subject: str, order: Order, tp: str, to: [] = adminEmails) -> bool:
    html = template.Template(tp)
    content = html.render(context=Context({'order': order}))
    print(content)
    message = EmailMultiAlternatives(subject, content, fromEmail, to)
    message.content_subtype = 'html'
    result = message.send()
    return result == 1

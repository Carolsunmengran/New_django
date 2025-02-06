from django.http import HttpResponse
from django.shortcuts import render

from common.models import Customer


# Create your views here.

def listorders(request):
    return HttpResponse('下面是系统中的所有订单信息1。。。')


def your_root_view_function(request):
    return HttpResponse('欢迎访问这个网站！这里是您的根路径视图内容。')


def listcustomers(request):
    # 返回一个QuerySet对象，包含所有表的记录
    # 每一条记录都是一个dict对象
    # 其中key是字段名，value是字段值
    qs = Customer.objects.values()

    # 检查URL中是否有phonenumber的值
    ph = request.GET.get('phonenumber', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    reStr = ''
    for customer in qs:
        for name, value in customer.items():
            reStr += f'{name} : {value} | '

        reStr += '<br>'

    return HttpResponse(reStr)

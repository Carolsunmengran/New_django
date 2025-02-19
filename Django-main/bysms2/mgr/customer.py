import json
from django.http import JsonResponse
from common.models import Customer


def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    print('请求方法是',request.method)
    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_customer':
        print("进入逻辑")
        return listcustomers(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listcustomers(request):
    qs = Customer.objects.values()
    print(qs)
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})


def addcustomer(request):
    info = request.params['data']
    print(info)
    record = Customer.objects.create(
        name=info['name'],
        phonenumber=info['phonenumber'],
        address=info['address']
    )
    return JsonResponse({'ret': 0, 'id': record.id})


def modifycustomer(request):
    customerid = request.params['id']
    newdata = request.params['newdata']

    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'id为{customerid}的用户不存在'}, status=404)

    if 'name' in newdata:
        customer.name = newdata['name']
    if 'phonenumber' in newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        customer.address = newdata['address']

    customer.save()
    return JsonResponse({'ret': 0})


def deletecustomer(request):
    customerid = request.params['id']

    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'id为{customerid}用户不存在'}, status=404)

    customer.delete()
    return JsonResponse({'ret': 0})

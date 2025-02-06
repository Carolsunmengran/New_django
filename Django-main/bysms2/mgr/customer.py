import json
from django.http import JsonResponse
from common.models import Customer

def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    # 检查action的存在性
    action = request.params.get('action')
    if not action:
        return JsonResponse({'ret': 1, 'msg': '缺少 action 参数'})

    if action == 'list_customer':
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
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})

def addcustomer(request):
    info = request.params['data']
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

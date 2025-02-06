import json
from django.http import JsonResponse
from common.models import Medicine


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

    if action == 'list_medicine':
        return listmedicine(request)
    elif action == 'add_medicine':
        return addmedicine(request)
    elif action == 'modify_medicine':
        return modifymedicine(request)
    elif action == 'del_medicine':
        return deletemedicine(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listmedicine(request):
    qs = Medicine.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})


def addmedicine(request):
    info = request.params['data']
    record = Medicine.objects.create(
        desc=info['desc'],
        name=info['name'],
        sn=info['sn']
    )
    return JsonResponse({'ret': 0, 'id': record.id})


def modifymedicine(request):
    medicineid = request.params['id']
    newdata = request.params['newdata']

    try:
        medicine = Medicine.objects.get(id=medicineid)
    except Medicine.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'id为{medicineid}的用户不存在'}, status=404)

    if 'name' in newdata:
        medicine.name = newdata['name']
    if 'phonenumber' in newdata:
        medicine.desc = newdata['desc']
    if 'address' in newdata:
        medicine.sn = newdata['sn']

    medicine.save()
    return JsonResponse({'ret': 0})


def deletemedicine(request):
    medicineid = request.params['id']

    try:
        medicine = Medicine.objects.get(id=medicineid)
    except Medicine.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'id为{medicineid}用户不存在'}, status=404)

    medicine.delete()
    return JsonResponse({'ret': 0})

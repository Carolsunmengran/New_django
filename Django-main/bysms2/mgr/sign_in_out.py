from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def signin(request):
    # 从HTTP POST请求中获取搭配用户名以及密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 使用Django auth库中的方法来校验用户名以及密码
    user = authenticate(username=userName, password=passWord)

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                request.session['usertype'] = 'mgr'
                # 在session中存入用户类型
                return JsonResponse({'ret': 0})

            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账号登录'})

        else:
            return JsonResponse({'ret': 1, 'msg': '用户已经被禁用'})

    else:
        return JsonResponse({'ret': 1, 'msg': '用户不存在'})


def signout(request):
    logout(request)
    # 使用退出方法
    return JsonResponse({'ret': 0})

from django.contrib import admin

# 导入一个include函数
from django.urls import path, include

# 静态文件服务
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 凡是 url 以 sales/  开头的，
    # 都根据 sales.urls 里面的 子路由表进行路由
    path('sales/', include('sales.urls')),

    # 凡是 url 以 api/mgr  开头的，
    # 都根据 mgr.urls 里面的 子路由表进行路由
    path('api/mgr/', include('mgr.urls')),

]  +  static("/", document_root="./z_dist")
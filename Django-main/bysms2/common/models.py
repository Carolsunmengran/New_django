from django.db import models
from django.contrib import admin



# Create your models here.

class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)
    # 联系电话
    phonenumber = models.CharField(max_length=200)
    # 地址
    address = models.CharField(max_length=200)

    # QQ
    QQ=models.CharField(max_length=30,null=True,blank=True)


admin.site.register(Customer)

class Medicine(models.Model):
    # 药品名称
    name = models.CharField(max_length=200)
    # 药品编号
    sn = models.CharField(max_length=200)
    # 药品描述
    desc = models.CharField(max_length=200)

admin.site.register(Medicine)

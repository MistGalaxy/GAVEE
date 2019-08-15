from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings
from docofgavee.settings import *
from  django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here
from django.contrib.auth import authenticate, login
from user.models import *
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    wechat_number =models.CharField(max_length=30)
    qq_number =models.CharField(max_length=30)
    phone_number =models.CharField(max_length=30)
    start_log =models.CharField(max_length=30)
    follow_person = models.ForeignKey(Myuser,on_delete=models.SET_NULL,null=True,blank=True)
    add_time = models.DateTimeField(default=now)
    def __str__(self):
        return  self.name
    class Meta:
        #修改admin后台显示名字
        verbose_name = "客户"
        verbose_name_plural = verbose_name

class FollowLog(models.Model):
    follow_person = models.ForeignKey(Myuser,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="客服")
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name="客户")
    log = models.CharField(max_length=200,verbose_name="跟进记录")
    add_time=models.DateTimeField(default=now,verbose_name="记录更新时间")
    follow_time = models.DateTimeField(default=now,verbose_name="跟进时间")

    def __str__(self):
        return  self.log
    class Meta:
        #修改admin后台显示名字
        verbose_name = "跟进记录"
        verbose_name_plural = verbose_name

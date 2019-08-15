from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings
from docofgavee.settings import *
from  django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here
from django.contrib.auth import authenticate, login
class Job(models.Model):
    job = models.CharField(max_length=10,choices=[('1',"CEO"),('2',"manage"),('3',"staff")])
    def __str__(self):
        return self.job

class Myuser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='资料')
    name = models.CharField(max_length=10,null=False)
    birthday = models.DateField(null=True,blank=True,default="1970/11/11")
    job = models.ForeignKey(Job,on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=300,null=True,blank=True)
    is_married = models.CharField(max_length=10,choices=[("1","YES"),('0',"NO"),('2',"unknown")])
    email = models.CharField(max_length=50,null=True,blank=True)
    sex = models.CharField(max_length=10,choices=[('1',"male"),('0',"female"),('2',"unknown")])
    phone_number = models.CharField(max_length=11,null=True,blank=True,)
    icon = models.ImageField(verbose_name="头像",upload_to="icon",null=True,blank=True)
    add_time =  models.DateTimeField(default=now)
    def __str__(self):
        return self.name
    def img_show(self):
        try:
            img = mark_safe('<img src="/media/%s" width="50px" />' % (self.icon))
        except Exception as e:
            img = ''
        return img
    img_show.short_description = '头像'
    img_show.allow_tags = True


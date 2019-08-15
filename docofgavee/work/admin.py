from django.contrib import admin
from work.models import *
# Register your models here.
@admin.register(Customer)
class Customer_admin(admin.ModelAdmin):
    list_display = ["name","follow_person","address","wechat_number","qq_number","phone_number","start_log","follow_person","add_time"]


@admin.register(FollowLog)
class FollowLog_admin(admin.ModelAdmin):
    list_display = ["customer","log","follow_person","add_time","follow_time"]


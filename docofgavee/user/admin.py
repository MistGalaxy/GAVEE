from django.contrib import admin
from user.models import *

# Register your models here.
class Useradmin(admin.ModelAdmin):
    pass


@admin.register(Myuser)
class UserAdmin(admin.ModelAdmin):

    list_display=( 'username', 'job_display', 'phone_number','img_show')
    search_fields = ['username', 'job', 'phone_number']
    def username(self,obj):
        return obj.user.username
    def job_display(self,obj):
        return obj.job.get_job_display()


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
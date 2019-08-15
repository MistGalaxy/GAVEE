from django.db import models

# Create your models here.
class goods(models.Model):

    name = models.CharField(max_length=20)
    nuber = models.IntegerField()
    out_log = models.ForeignKey()
    add_log =  models.ForeignKey()
    goods_color = models.CharField(max_length=20)

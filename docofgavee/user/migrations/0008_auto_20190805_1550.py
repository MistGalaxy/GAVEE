# Generated by Django 2.2.3 on 2019-08-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190805_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Users\\J\\Desktop\\GAVEE\\docofgavee\\media', verbose_name='头像'),
        ),
    ]

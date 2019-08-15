# Generated by Django 2.2.4 on 2019-08-15 03:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0020_myuser_add_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('wechat_number', models.CharField(max_length=30)),
                ('qq_number', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('start_log', models.CharField(max_length=30)),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('follow_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Myuser')),
            ],
        ),
        migrations.CreateModel(
            name='FollowLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=200, verbose_name='跟进记录')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='记录更新时间')),
                ('follow_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='跟进时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Customer', verbose_name='客户')),
                ('follow_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Myuser', verbose_name='客服')),
            ],
        ),
    ]

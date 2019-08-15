# Generated by Django 2.2.3 on 2019-08-05 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(choices=[(1, 'CEO'), (2, 'manage'), (3, 'staff')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('birthday', models.DateField(blank=True, default='1970/11/11', null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('is_married', models.CharField(choices=[(1, 'YES'), (0, 'NO'), (2, 'unknown')], max_length=10)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(choices=[(1, 'men'), (0, 'female'), (2, 'unknown')], max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Job')),
            ],
        ),
    ]
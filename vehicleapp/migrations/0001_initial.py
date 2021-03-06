# Generated by Django 4.0.2 on 2022-02-19 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=10000)),
                ('is_seen', models.BooleanField(default=False)),
                ('isdate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='vehicledetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vehicleno', models.CharField(max_length=100)),
                ('speed', models.FloatField()),
                ('avgspeed', models.FloatField()),
                ('temperature', models.IntegerField()),
                ('fuellevel', models.IntegerField()),
                ('enginestatus', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-06-11 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0009_auto_20210611_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='alive_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 20, 59, 43, 866513)),
        ),
        migrations.AlterField(
            model_name='token',
            name='assigned_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 20, 59, 43, 866513)),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 20, 59, 43, 866513)),
        ),
        migrations.AlterField(
            model_name='token',
            name='unassigned_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 20, 59, 43, 866513)),
        ),
    ]
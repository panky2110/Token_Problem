# Generated by Django 3.2 on 2021-06-11 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0005_auto_20210611_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='alive_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 19, 40, 16, 504212)),
        ),
        migrations.AlterField(
            model_name='token',
            name='assigned_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 19, 40, 16, 504212)),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 19, 40, 16, 504212)),
        ),
        migrations.AlterField(
            model_name='token',
            name='unassigned_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 19, 40, 16, 504212)),
        ),
    ]

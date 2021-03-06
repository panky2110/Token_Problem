# Generated by Django 3.2 on 2021-06-15 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0012_auto_20210615_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='assigned_time',
        ),
        migrations.AddField(
            model_name='token',
            name='assigned_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 10, 46, 31, 66664)),
        ),
        migrations.AddField(
            model_name='token',
            name='unassigned_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 10, 46, 31, 66664)),
        ),
        migrations.AlterField(
            model_name='token',
            name='alive_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 10, 46, 31, 66664)),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 10, 46, 31, 66664)),
        ),
    ]

# Generated by Django 3.2 on 2021-06-15 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0010_auto_20210612_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='alive_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 9, 57, 8, 711036)),
        ),
        migrations.AlterField(
            model_name='token',
            name='assigned_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 9, 57, 8, 711036)),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 9, 57, 8, 711036)),
        ),
        migrations.AlterField(
            model_name='token',
            name='unassigned_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 9, 57, 8, 711036)),
        ),
    ]

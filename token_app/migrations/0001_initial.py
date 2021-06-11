# Generated by Django 3.2 on 2021-06-11 03:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=datetime.datetime(2021, 6, 11, 9, 25, 41, 26094))),
                ('token_name', models.CharField(db_index=True, max_length=80, unique=True)),
                ('is_assigned', models.BooleanField(default=False)),
                ('assigned_at', models.DateTimeField(default=datetime.datetime(2021, 6, 11, 3, 55, 41, 26094, tzinfo=utc))),
                ('unassigned_at', models.DateTimeField(default=datetime.datetime(2021, 6, 11, 3, 55, 41, 26094, tzinfo=utc))),
                ('is_alive', models.BooleanField(default=False)),
                ('alive_at', models.DateTimeField(default=datetime.datetime(2021, 6, 11, 3, 55, 41, 26094, tzinfo=utc))),
            ],
            options={
                'db_table': 'Token',
            },
        ),
    ]
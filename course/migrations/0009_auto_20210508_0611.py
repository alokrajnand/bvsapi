# Generated by Django 3.2 on 2021-05-08 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20210508_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 6, 11, 33), null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 6, 11, 33), null=True),
        ),
    ]
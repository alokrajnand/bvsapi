# Generated by Django 3.2 on 2021-05-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210521_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_like',
            field=models.IntegerField(default='100'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_reviewed',
            field=models.IntegerField(default='100'),
        ),
    ]

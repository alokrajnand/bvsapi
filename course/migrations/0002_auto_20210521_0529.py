# Generated by Django 3.2 on 2021-05-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lesson_count',
            field=models.IntegerField(default='10'),
        ),
        migrations.AddField(
            model_name='course',
            name='total_enrolled',
            field=models.IntegerField(default='10'),
        ),
    ]

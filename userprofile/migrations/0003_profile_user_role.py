# Generated by Django 3.2 on 2021-05-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20210512_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_role',
            field=models.CharField(default='User', max_length=200),
        ),
    ]
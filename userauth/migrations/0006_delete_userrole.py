# Generated by Django 3.2 on 2021-05-13 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_userrole'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]

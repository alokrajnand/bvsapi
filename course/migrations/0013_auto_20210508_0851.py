# Generated by Django 3.2 on 2021-05-08 08:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20210508_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 8, 51, 26), null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 8, 51, 26), null=True),
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rated_by', models.CharField(max_length=50, unique=True)),
                ('rating', models.CharField(max_length=100, null=True)),
                ('rating_comment', models.CharField(max_length=50, null=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('course_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', to_field='course_header')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-05-20 13:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussion_header', models.CharField(default='', max_length=50, unique=True)),
                ('course_name', models.CharField(max_length=50)),
                ('lesson_name', models.CharField(max_length=50)),
                ('discussion_name', models.CharField(default='', max_length=50, unique=True)),
                ('discussion_desc', models.CharField(max_length=50)),
                ('discussion_views', models.IntegerField(null=True)),
                ('discussion_ans_count', models.IntegerField(null=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('course_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', to_field='course_header')),
                ('lesson_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lesson', to_field='lesson_header')),
            ],
        ),
    ]

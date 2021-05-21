# Generated by Django 3.2 on 2021-05-20 13:29

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_email_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='userauth.user')),
                ('user_name', models.CharField(max_length=200)),
                ('user_date_of_birth', models.DateField()),
                ('user_role', models.CharField(default='User', max_length=200)),
                ('user_phone_number', models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='phone number is not valid', regex='^\\+?1?\\d{9,15}$')])),
                ('user_class', models.CharField(max_length=200, null=True)),
                ('user_aim', models.CharField(max_length=200, null=True)),
                ('user_designation', models.CharField(max_length=200, null=True)),
                ('user_tag_line', models.CharField(max_length=200, null=True)),
                ('user_tag_line_desc', models.CharField(max_length=300, null=True)),
                ('user_profile_pic_link', models.CharField(max_length=200, null=True)),
                ('user_banner_pic_link', models.CharField(max_length=200, null=True)),
                ('user_address', models.CharField(max_length=200, null=True)),
                ('user_city', models.CharField(max_length=60, null=True)),
                ('user_state', models.CharField(max_length=60, null=True)),
                ('user_country', models.CharField(max_length=60, null=True)),
                ('user_twitter_link', models.CharField(max_length=200, null=True)),
                ('user_git_hub_link', models.CharField(max_length=200, null=True)),
                ('user_linkdin_link', models.CharField(max_length=200, null=True)),
                ('user_faebook_link', models.CharField(max_length=200, null=True)),
                ('user_instagram_link', models.CharField(max_length=200, null=True)),
                ('user_created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('user_updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-16 21:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, verbose_name='user_name')),
                ('first_name', models.CharField(max_length=50, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last_name')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='phone must be an egyptian phone number...', regex='^01[1|0|2|5][0-9]{8}$')], verbose_name='phone')),
                ('photo', models.ImageField(upload_to='images', verbose_name='photo')),
                ('is_active', models.BooleanField(default=False)),
                ('facebook_link', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('date_birth', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-17 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportproject',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_reaction', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

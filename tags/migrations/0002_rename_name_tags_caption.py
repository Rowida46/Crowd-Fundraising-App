# Generated by Django 4.1.7 on 2023-03-12 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='name',
            new_name='caption',
        ),
    ]

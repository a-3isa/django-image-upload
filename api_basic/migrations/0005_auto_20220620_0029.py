# Generated by Django 3.2.13 on 2022-06-19 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0004_auto_20220620_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image_1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='image_2',
            new_name='style',
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-20 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0006_article_artwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
    ]

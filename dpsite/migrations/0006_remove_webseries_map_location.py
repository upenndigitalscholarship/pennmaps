# Generated by Django 2.0.6 on 2018-07-24 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0005_auto_20180724_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webseries',
            name='map_location',
        ),
    ]

# Generated by Django 2.0.6 on 2018-07-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0003_auto_20180724_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webseries',
            name='map_location',
            field=models.ManyToManyField(blank=True, to='dpsite.MapItem', verbose_name='Map'),
        ),
    ]

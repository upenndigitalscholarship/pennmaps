# Generated by Django 2.0.6 on 2018-07-26 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0012_auto_20180726_0644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mapitem',
            options={'ordering': ['title'], 'verbose_name': 'Map Item', 'verbose_name_plural': 'Map Items'},
        ),
    ]
# Generated by Django 2.0.6 on 2018-07-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0011_tag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

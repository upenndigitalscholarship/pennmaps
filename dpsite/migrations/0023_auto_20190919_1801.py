# Generated by Django 2.2.5 on 2019-09-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0022_siteconfig_map_sidebar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partofcity',
            options={'verbose_name': 'Part of City', 'verbose_name_plural': 'Parts of City'},
        ),
        migrations.AddField(
            model_name='media',
            name='file_iframe',
            field=models.CharField(blank=True, help_text='Please paste in an &lt;iframe&gt; to embed external content. Content must begin with &lt;iframe&gt; and end with &lt;/iframe&gt; ', max_length=1000, null=True, verbose_name='File <iframe>'),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

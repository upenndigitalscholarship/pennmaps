# Generated by Django 2.0.6 on 2018-06-20 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0003_auto_20180619_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverlayGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TagGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='mapitem',
            name='media',
        ),
        migrations.AddField(
            model_name='mapitem',
            name='media',
            field=models.ManyToManyField(to='dpsite.Media'),
        ),
        migrations.RemoveField(
            model_name='mapitem',
            name='overlay_group',
        ),
        migrations.RemoveField(
            model_name='mapitem',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='media',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='webseries',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpsite.TagGroup'),
        ),
        migrations.AddField(
            model_name='mapitem',
            name='overlay_group',
            field=models.ManyToManyField(to='dpsite.OverlayGroup'),
        ),
        migrations.AddField(
            model_name='mapitem',
            name='tags',
            field=models.ManyToManyField(to='dpsite.Tag'),
        ),
        migrations.AddField(
            model_name='media',
            name='tags',
            field=models.ManyToManyField(to='dpsite.Tag'),
        ),
        migrations.AddField(
            model_name='webseries',
            name='tags',
            field=models.ManyToManyField(to='dpsite.Tag'),
        ),
    ]

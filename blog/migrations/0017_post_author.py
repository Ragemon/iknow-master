# Generated by Django 2.1.4 on 2019-01-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190101_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.TextField(default='Courage'),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181225_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=120)),
        ),
    ]

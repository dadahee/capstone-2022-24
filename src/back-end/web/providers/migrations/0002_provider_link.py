# Generated by Django 4.0.4 on 2022-05-17 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='link',
            field=models.URLField(default='https://default_ott_link.com'),
        ),
    ]

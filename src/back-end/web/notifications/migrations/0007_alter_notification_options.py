# Generated by Django 4.0.4 on 2022-06-03 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_alter_notificationcontent_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ('-creation_date_time',)},
        ),
    ]

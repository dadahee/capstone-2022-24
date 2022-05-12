# Generated by Django 4.0.4 on 2022-05-12 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '__first__'),
        ('groups', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fellow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('will_renew', models.BooleanField(default=True)),
                ('creation_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modification_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('has_reported', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fellow',
                'ordering': ('-creation_date_time',),
                'unique_together': {('user', 'group')},
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_reported_leader', models.BooleanField(default=False)),
                ('fellow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='fellows.fellow')),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fellow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='fellows.fellow')),
            ],
            options={
                'db_table': 'leader',
            },
        ),
    ]

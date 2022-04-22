# Generated by Django 4.0.3 on 2022-04-21 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StarRating',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value', models.FloatField(choices=[(0.5, '0.5'), (1.0, '1'), (1.5, '1.5'), (2.0, '2'), (2.5, '2.5'), (3.0, '3'), (3.5, '3.5'), (4.0, '4'), (4.5, '4.5'), (5.0, '5')], default=5)),
                ('date_time', models.DateTimeField(db_column='dateTime', default=django.utils.timezone.now)),
                ('user', models.ForeignKey(db_column='userId', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(db_column='videoId', on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
            options={
                'db_table': 'star_ratings',
            },
        ),
    ]

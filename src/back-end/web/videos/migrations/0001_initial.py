# Generated by Django 4.0.4 on 2022-05-12 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.BigIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('release_date', models.DateField(null=True)),
                ('film_rating', models.CharField(max_length=10, null=True)),
                ('category', models.CharField(choices=[('TV', 'TVSeries'), ('MV', 'Movie')], max_length=2)),
                ('poster_key', models.URLField(null=True)),
                ('title_english', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'videos',
            },
        ),
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('video', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='videos.video')),
                ('runtime', models.PositiveIntegerField(null=True)),
            ],
            options={
                'db_table': 'video_details',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.FloatField(max_length=10)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='ProductionCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
            options={
                'db_table': 'production_countries',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
            options={
                'db_table': 'genres',
            },
        ),
    ]

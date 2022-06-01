# Generated by Django 4.0.4 on 2022-06-01 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tv_details', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvseasondetail',
            name='tmdb_number',
        ),
        migrations.RemoveField(
            model_name='tvseasondetail',
            name='trailer_key',
        ),
        migrations.RemoveField(
            model_name='tvseasondetail',
            name='video',
        ),
        migrations.AddField(
            model_name='tvseasondetail',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tvseriesdetail',
            name='trailer_key',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tvseason',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tv_details.tvseriesdetail'),
        ),
    ]

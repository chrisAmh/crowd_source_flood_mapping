# Generated by Django 5.0.6 on 2024-06-05 23:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodzones', '0002_rename_remotesensingimage_floodimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='floodimage',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AddField(
            model_name='floodimage',
            name='taken_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='floodimage',
            name='title',
            field=models.CharField(default='No title provided', max_length=100),
        ),
        migrations.AddIndex(
            model_name='floodimage',
            index=models.Index(fields=['latitude', 'longitude'], name='floodzones__latitud_5caad9_idx'),
        ),
        migrations.AddField(
            model_name='comment',
            name='flood_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='floodzones.floodimage'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

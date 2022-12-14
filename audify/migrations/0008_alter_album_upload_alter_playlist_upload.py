# Generated by Django 4.0 on 2022-08-18 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audify', '0007_alter_artist_upload_alter_playlist_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='upload',
            field=models.ImageField(upload_to='albums/%c/'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='upload',
            field=models.ImageField(blank=True, upload_to='playlists/%c/'),
        ),
    ]

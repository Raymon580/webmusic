# Generated by Django 4.0 on 2022-08-18 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audify', '0008_alter_album_upload_alter_playlist_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='upload',
            field=models.ImageField(upload_to='artists/% Y/% m/% d/'),
        ),
    ]

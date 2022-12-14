# Generated by Django 4.0 on 2022-08-17 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audify', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('upload', models.ImageField(upload_to='media/artists/<django.db.models.fields.CharField>/% Y/% m/% d/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='audify.artist')),
                ('ft_artists', models.ManyToManyField(blank=True, to='audify.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='allGenreSongs', to='audify.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('upload', models.ImageField(blank=True, upload_to='media/playlists/<django.db.models.query_utils.DeferredAttribute object at 0x000001FADAE5B340>/% Y/% m/% d/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='audify.user')),
                ('songs', models.ManyToManyField(to='audify.Song')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('upload', models.ImageField(upload_to='media/albums/<django.db.models.fields.related.ForeignKey>/<django.db.models.fields.CharField>/% Y/% m/% d/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='audify.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='allGenreAlbums', to='audify.genre')),
                ('songs', models.ManyToManyField(to='audify.Song')),
            ],
        ),
    ]

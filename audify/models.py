from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class Artist(models.Model):
    name = models.CharField(max_length=64)
    upload = models.ImageField(upload_to = 'artists')

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre = models.CharField(max_length=32)

    def __str__(self):
        return self.genre


class Song(models.Model):
    title = models.CharField(max_length=64)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    ft_artists = models.ManyToManyField(Artist, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="allGenreSongs")


class Album(models.Model):
    title = models.CharField(max_length=64)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    songs = models.ManyToManyField(Song)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="allGenreAlbums")
    upload = models.ImageField(upload_to = 'albums')


class Playlist(models.Model):
    title = models.CharField(max_length=128)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    songs = models.ManyToManyField(Song)
    upload = models.ImageField(upload_to = 'playlists', blank=True)
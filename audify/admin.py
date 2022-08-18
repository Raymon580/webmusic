from django.contrib import admin
from .models import Album, Artist, Genre, Playlist, Song, User

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
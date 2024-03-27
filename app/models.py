from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length = 20)
    album = models.ImageField(upload_to = 'albums/')
    audio = models.FileField(upload_to='musics/')

    def __str__(self):
        return self.title

class Folder(models.Model):
    name = models.CharField(max_length=20, default='fav')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    music_track = models.ManyToManyField(Music)
    
    def __str__(self):
        return self.name
    
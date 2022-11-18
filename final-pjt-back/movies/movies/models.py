from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    youtube_key = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    actors = models.ManyToManyField(Actor)

class Nowplaying(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    youtube_key = models.CharField(max_length=100)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rank_choices = ((5, '★★★★★'),(4, '★★★★'),(3, '★★★'),(2, '★★'),(1, '★'))
    rank = models.IntegerField(choices=rank_choices)
    good_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='good_rewiews')
    bad_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bad_rewiews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

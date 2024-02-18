from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.genre

class Artist(models.Model):
    artist = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.artist

class Movie(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_year = models.IntegerField()
    movie_art =  models.ImageField(upload_to='')
    
    def __str__(self) -> str:
        return self.title
    

  
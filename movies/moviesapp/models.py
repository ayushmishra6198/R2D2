from django.db import models

# Create your models here.

class MovieList(models.Model):

    movie_id = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=200)
    movie_cast = models.CharField(max_length=200)
    movie_ratings = models.CharField(max_length=4)


    def __str__(self):
        return str(self.movie_id)


    def get_absolute_url(self):
        return reverse('movieSearch', args=[(self.movie_name)])


    def Meta():
        ordering = ['movie_ratings']

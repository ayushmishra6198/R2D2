from rest_framework import serializers
from .models import MovieList


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = ('movie_id','movie_name','movie_cast','movie_ratings')

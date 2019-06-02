from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import MovieList

# Register your models here.


@admin.register(MovieList)
class MovieListAdmin(admin.ModelAdmin):
    list_display = ('movie_id','movie_name')

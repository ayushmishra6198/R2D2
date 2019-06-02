from django.conf.urls import url
from django.urls import path, re_path
from . import views



urlpatterns = [

    path('',views.index, name='index'),
    #url(r'^moviesapp/(?P<movie>\w{0,50})$', views.movieSearch, name = "movieSearch"),
    re_path(r'^moviesapp/(?P<movie>\w{0,50})$', views.movieSearch, name = "movieSearch"),
    #re_path(r'^moviesapp/\w+)$', views.movieSearch, name = 'movieSearch'),
    #re_path(r'^moviesapp/?(\w+)', views.movieSearch, name = 'movieSearch'),
    url(
        r'^api/v1/moviesapp/(?P<pk>[0-9]+)$',
        views.get_movieList,
        name = 'get_movieList'
        ),
 #   url(        r'^api/v1/moviesapp/<str:movie_name>',        views.get_movieList,        name = 'get_movieList'        ),
    url(
        r'^api/v1/moviesapp/$',
        views.get_movieGP,
        name = 'get_movieGP'
        )
    ]

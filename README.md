# R2D2
Python Home Assingment

Clone The Repository.

(https://github.com/ayushmishra6198/R2D2.git)

Create Database (postgresql is used )

(python manage.py migrate)

Run the server 

(python manage.py runserver)


for searching a movie through name use:-

-> type the movie name in the search box (case sensitive eg:Avengers not avengers). the list will appear.

(eg:-http://127.0.0.1:8000/moviesapp/?csrfmiddlewaretoken=rs9gVqvAI98opP4z2apQQSkCCAxbMQlt3C8pxvaexBF2KE2kWQgSLmGUhh5bFc54&movie=Avengers)




to search movie id through api use:-

->http://127.0.0.1:8000/api/v1/moviesapp/Movie_id           (eg:-http://127.0.0.1:8000/api/v1/moviesapp/1)



1<Movie_id<1391






The Scrapping of movie is done through imdb site.

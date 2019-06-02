from django import forms


class SearchMovie(forms.Form):
    movie_name = forms.CharField(label="Search Movie : ", max_length=40)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MovieList
from .serializers import MovieListSerializer
from .forms import SearchMovie

# Create your views here.

def index(request):
    mse = SearchMovie()
    movies = MovieList.objects.all()
    context = {'movies' : movies, "form":mse}
        
    return render(request, 'index.html', context)
    

def movieSearch(request, movie=None):
    sertext = request.GET['movie']
    try:
        movies = MovieList.objects.filter(movie_name__contains=sertext)[:5]
        if not movies:
            movies = MovieList.objects.filter(movie_id__contains=sertext)
    except MovieList.DoesNotExist:
        return render(request, status=status.HTTP_404_NOT_FOUND)
        
    context = {'movies' : movies}
    return render(request, 'index.html', context)




@api_view(['GET'])
def get_movieList(request, pk):       
    
    if request.method == 'GET':
        try:
            movies = MovieList.objects.get(pk=pk)
            serializer = MovieListSerializer(movies, many=False)
            return Response(serializer.data)
        except MovieList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
'''
    if request.method == 'DELETE':
        return Response({})

    if request.method == 'PUT':
        return Response({})
        
'''

@api_view(['GET','POST'])
def get_movieGP(request):

    if request.method == 'GET':
        # Empty Code not used yet
        return Response({})
    

    if request.method == 'POST':
        # Empty Code not used yet
        return Response({})

    

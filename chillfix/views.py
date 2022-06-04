from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .request import get_moviez, get_movie, get_youtube

# Create your views here.
def home(request):
    popularMovies = get_moviez('popular')
    
    return render(request, 'index.html', {'popularMovies':popularMovies})

def movies(request , movie_id):
    one_movie = get_movie(movie_id)
    movie = get_movie(movie_id)
    youtube_id = get_youtube(movie['title'])
    youtube_url = f'https://www.youtube.com/embed/{youtube_id}?autoplay=1&muted=0'
    return render(request, 'details.html', {'one_movie':one_movie, 'youtube_url':youtube_url})


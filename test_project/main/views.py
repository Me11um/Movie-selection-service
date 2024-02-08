from django.shortcuts import render
from .movies.getmovies import *

# Create your views here.
def index(request):
    data = {
        'title': 'Сервис для подброки фильмов',
        'movies': filteredmovies,
        'images': filteredimages
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
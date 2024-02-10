from django.shortcuts import render
from .movies.getmovies import *

# Create your views here.
def index(request):
    data = {
        'title': 'Сервис для подборки фильмов'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def app(request):
    if request.method == "POST":
        data = getmoviesname(request.POST.get("genre"))
        return render(request, 'main/app.html', data)
    else:
        data = {
            'movies': [],  # filteredmovies,
            'images': [],  # filteredimages
            'genre': [],
            'year': [],
            'rating': [],
            'hrefs': []
        }
        return render(request, 'main/app.html', data)
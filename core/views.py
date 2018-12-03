from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    """
    View representing all objects(movies)
    """
    model = Movie


class MovieDetail(DetailView):
    """
    View representing an Individual object(movie)
    """
    model = Movie






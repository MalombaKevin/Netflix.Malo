from django.urls import path
from chillfix import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('details/<int:movie_id>', views.movies, name='movies'),
]

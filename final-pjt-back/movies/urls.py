from django.urls import path
from . import views_tmdb, views

urlpatterns = [
    path('', views.movie_list),
    path('tmdb/', views_tmdb.tmdb_data),
    path('now/', views.now_movie_list)
]

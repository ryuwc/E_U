from django.urls import path
from . import views_tmdb

urlpatterns = [
    path('tmdb/', views_tmdb.tmdb_data),
]

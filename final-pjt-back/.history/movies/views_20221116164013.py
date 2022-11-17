from movies.models import Movie
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from movies.serializers import MovieListSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

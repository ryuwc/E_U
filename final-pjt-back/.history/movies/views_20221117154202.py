from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_list_or_404
from movies.serializers import MovieListSerializer, NowMovieListSerializer
from movies.models import Movie,Nowplaying

@api_view(['GET', 'POST'])
# get요청은 인증이 필요없고, post요청은 인증이 필요하다.
# @permission_classes([IsAuthenticatedOrReadOnly])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by())
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def now_movie_list(request):
    if request.method == 'GET':
        nowmovie = get_list_or_404(Nowplaying.objects.order_by())
        serializer= NowMovieListSerializer(nowmovie, many=True)
        return Response(serializer.data)

        
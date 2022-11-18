from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes
from .forms import MovieForm, ReviewForm
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from movies.serializers import MovieListSerializer, MovieSerializer, NowMovieListSerializer, ReviewSerializer
from movies.models import Movie, Nowplaying, Review

@api_view(['GET', 'POST'])
# get요청은 인증이 필요없고, post요청은 인증이 필요하다.
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by())
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm()
    reviews = movie.review_set.all()

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def now_movie_list(request):
    if request.method == 'GET':
        nowmovie = get_list_or_404(Nowplaying.objects.order_by())
        serializer= NowMovieListSerializer(nowmovie, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_detail(request, review_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_list_create(request, movie_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
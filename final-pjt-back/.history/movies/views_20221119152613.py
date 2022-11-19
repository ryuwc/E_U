from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from movies.serializers import MovieListSerializer, MovieSerializer, NowMovieListSerializer, ReviewSerializer, ReviewListSerializer, ReviewCreateSerializer
from movies.models import Movie, Nowplaying, Review

@api_view(['GET', 'POST'])
# get요청은 인증이 필요없고, post요청은 인증이 필요하다.
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by())
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def now_movie_list(request):
    nowmovie = get_list_or_404(Nowplaying.objects.order_by())
    serializer= NowMovieListSerializer(nowmovie, many=True)
    return Response(serializer.data)

# movie_Detail -> 전체 리뷰 조회(GET) 리뷰 생성(POST)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_list_create(request, movie_pk):
  if request.method == 'GET':
    reviews = Review.objects.filter(movie_id=movie_pk)
    # 외래키의 movie_id가 movie_pk와 일치하는 경우 .filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    # 복수 객체
    return Response(serializer.data)
  else:
  # 생성(POST)
    # movie = get_object_or_404(Movie, pk=movie_pk)
    # serializer = ReviewSerializer(data=request.data)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save(user=request.user, movie = movie)
    #     # user, movie 외래키 참조 객체 설정
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 2022.11.19 류원창 수정
    review = get_object_or_404(Review, pk=movie_pk)
    serializer = ReviewCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie = review)
        # user, movie 외래키 참조 객체 설정
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def review_detail(request, review_pk):
# movie_Detail -> 리뷰 조회(GET), 수정(PUT), 삭제(DELETE)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        if request.user == review.user:
            # 작성자와 같은 경우
            if request.method == 'DELETE':
                review.delete()
                data = {
                    f'{review_pk}번 리뷰가 삭제되었습니다.'
                }
                return Response(data, status=status.HTTP_204_NO_CONTENT)
            if request.method == 'PUT':
                serializer = ReviewSerializer(review, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
            # 작성자와 다른 경우
    



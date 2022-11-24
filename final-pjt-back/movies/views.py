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
from django.contrib.auth import get_user_model


@api_view(['GET', 'POST'])
# get요청은 인증이 필요없고, post요청은 인증이 필요하다.
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by())
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


# 영화 디테일 조회(GET), 영화 찜하기(POST)
# 찜할 때는 메서드는 그냥 POST로 data없이 보내면 된다. (보낼 때의 토큰이 해당 유저와 매칭시킨다.)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 조회(GET)일 경우
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    # 찜하기(POST)일 경우
    elif request.method == 'POST':
        # 찜하기는 로그인한 유저만 가능하다.
        # 찜하기를 누른 유저가 이미 찜을 눌렀는지 확인
        if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
            movie_like = False
        else:
            movie.like_users.add(request.user)
            movie_like = True
        context = {
            'msg': '찜하기 or 찜취소 접근 성공',
            'movie_like': movie_like,
        }
        return Response(context, status=status.HTTP_201_CREATED)


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
    # 리뷰 생성
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie = movie)
        # user, movie 외래키 참조 객체 설정
        context = {
            'message': '리뷰가 작성되었습니다.',
            'id': serializer.data.get('id'),
            'content': serializer.data.get('content'),
            'created_at': serializer.data.get('created_at'),
            'good_user': serializer.data.get('good_user'),
            'bad_user': serializer.data.get('bad_user'),
            'user': serializer.data.get('user'),
            'rank': serializer.data.get('rank'),
        }
        return Response(context, status=status.HTTP_201_CREATED)
    

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


# url: movies/review/<int:review_pk>/like/
# method: POST
# data: user_id
# 리뷰 좋아요
@api_view(['POST'])
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    print(user.id)
    if review.good_user.filter(pk=user.pk).exists():
        review.good_user.remove(user)
        is_liked = False
    else:
        review.good_user.add(user)
        is_liked = True
    context = {'is_liked': is_liked, 'count': review.good_user.count()}
    return Response(context, status=status.HTTP_200_OK)


# url: movies/review/<int:review_pk>/dislike/
# method: POST
# data: user_id
# 리뷰 싫어요
@api_view(['POST'])
def dislike(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.bad_user.filter(pk=user.pk).exists():
        review.bad_user.remove(user)
        disliked = False
    else:
        review.bad_user.add(user)
        disliked = True
    context = {'disliked': disliked, 'count': review.bad_user.count()}
    return Response(context, status=status.HTTP_200_OK)


# 특정 유저가 위시리스트에 담은 영화 목록 조회
# url: movies/wish/user_id/
# method: GET
# data필요 없이 토큰만 보내면 됨
@api_view(['GET', 'POST'])
def wish_list(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    print(user)
    movies = get_list_or_404(Movie, like_users=user)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 유저가 디테일 페이지 방문시 user_click필드 1증가
# url: movies/click/<int:movie_pk>/
# method: POST
# data필요 없음
@api_view(['POST'])
def user_click(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.user_click += 1
    movie.save()
    return Response({'msg': f'{movie_pk}번 영화의 클릭수가 1 증가했습니다.'}, status=status.HTTP_200_OK)

from django.urls import path
from movies import views_tmdb, views

# movies/ => enculde
urlpatterns = [
    
    # API 데이터 DB 저장
    path('tmdb/', views_tmdb.tmdb_data),
    # 전체 영화 조회(GET)
    path('', views.movie_list),
    # 현재 상영중인 영화 조회(GET)
    path('now/', views.now_movie_list),
    # movie_Detail 조회(GET)
    path('<int:movie_pk>/', views.movie_detail),
    # movie_Detail -> 전체 리뷰 조회(GET), 생성(POST)
    path('<int:movie_pk>/review/', views.review_list_create, name='review_list_create'),
    # movie_Detail -> 리뷰 조회(GET), 수정(PUT), 삭제(DELETE)   
    path('review/<int:review_pk>/', views.review_detail, name='review_detail'),

    # 2022.11.19 류원창 추가
    # 리뷰 좋아요, 싫어요 기능
    path('review/<int:review_pk>/like/', views.like, name='like'),
    path('review/<int:review_pk>/dislike/', views.dislike, name='dislike'),

    # 전체 위시리스트 조회(GET)
    # path('wish/', views.wish_list, name='wish_list'),

    # 특정 유저가 위시리스트에 추가한 영화 조회(GET)
    path('wish/<int:user_id>/', views.wish_list, name='wish_list'),

    # 유저가 영화 디테일 페이지에 오면 user_click +1
    path('click/<int:movie_pk>/', views.user_click, name='user_click'),
]

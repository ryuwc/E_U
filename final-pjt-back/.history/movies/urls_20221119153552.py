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
    # 리뷰 좋아요, 싫어요 기능
    path('review/<int:review_pk>/like/', views.like),
    path('review/<int:review_pk>/dislike/', views.dislike),

]

from django.urls import path
from . import views_tmdb, views

# movies/ => enculde
urlpatterns = [
    path('', views.movie_list),
    path('tmdb/', views_tmdb.tmdb_data),
    path('now/', views.now_movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    # path('reviews/', views.review_list),
    # path('reviews/<int:review_pk>/', views.review_detail),
    # path('<int:movie_pk>/reviews/', views.review_create),

    path('<int:movie_pk>/review/', views.review_list_create, name='review_list_create'),
    # 상세 영화 전체 리뷰 조회(GET) 리뷰 생성(POST)
    
    path('review/<int:review_pk>/', views.review_detail, name='review_detail'),
    # 상세 영화 상세 리뷰 조회(GET), 수정(PUT), 삭제(DELETE)
]

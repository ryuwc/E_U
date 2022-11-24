from django.urls import path
from comments import views
   
urlpatterns = [
    # 프로필 유저 생성
    path('profileuser/', views.profileuser_list, name='profileuser_list'),
  
    # 프로필 유저 전체 댓글 조회(GET)
    path('profileuser/<int:profile_pk>/comments/', views.comment_list, name='comment_list'),
    # 프로필 유저 댓글 생성(POST)
    path('profileuser/<int:profile_pk>/comment/', views.comment_create, name='comment_create'),
    # 프로필 유저 댓글 삭제 (DELETE)
    path('profileuser/<int:profile_pk>/comment/<int:comment_pk>/', views.comment_delete, name = 'comment_delete'),
]
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile_username, name='profile_username'),
]
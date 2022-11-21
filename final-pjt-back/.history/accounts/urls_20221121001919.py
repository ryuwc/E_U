from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<int:user_id>/', views.profile, name='profile'),
]
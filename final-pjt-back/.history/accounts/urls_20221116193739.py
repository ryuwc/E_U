from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<str:username>', views.profile, name='profile'),
]
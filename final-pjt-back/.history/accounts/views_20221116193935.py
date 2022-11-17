from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    return JsonResponse({
        'username': person.username,
        'email': person.email,
        'first_name': person.first_name,
        'last_name': person.last_name,
    })
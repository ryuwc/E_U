from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return JsonResponse(context)
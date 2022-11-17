from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from rest_framework.response import Response
from accounts.serializers import UserSerializer

# Create your views here.

# 유저 정보를 조회하기 위한 추가 코드 (제이슨 형식으로 리턴)
@require_POST
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(person)
    return Response(serializer.data)
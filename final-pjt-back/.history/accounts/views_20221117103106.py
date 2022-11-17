from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view




# Create your views here.

# 유저 정보를 조회하기 위한 추가 코드 (제이슨 형식으로 리턴)
# def profile(request, username):
#     person = get_object_or_404(get_user_model(), username=username)
#     serializer = UserSerializer(person)
#     return JsonResponse({
#         'username': person.username,
#         'nickname': person.nickname,
#         'profile_path': person.profile_path,
#     })

@api_view(['GET', 'PUT'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    print(request)
    serializer = UserSerializer(person)
    return Response(serializer.data)

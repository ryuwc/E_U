from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
# get_user_model()을 통해 현재 활성화된 유저 모델을 가져온다.
from django.contrib.auth import get_user_model

# nickname, profile_path 추가를 위한 CustomRegisterSerializer생성
class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20, required=False)
    profile_path = serializers.CharField(max_length=500, required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['profile_path'] = self.validated_data.get('profile_path', '')
        return data_dict
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'nickname', 'profile_path')

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
# get_user_model()을 통해 현재 활성화된 유저 모델을 가져온다.
from django.contrib.auth import get_user_model

# nickname, profile_path 추가를 위한 CustomRegisterSerializer생성
class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20, required=False)
    profile_path = serializers.CharField(max_length=10000, required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['profile_path'] = self.validated_data.get('profile_path', 'data:image/png;base64,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')
        return data_dict
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'nickname', 'profile_path')

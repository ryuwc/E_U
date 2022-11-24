from rest_framework import serializers
from comments.models import Profile, Comment

class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('profile', 'user')


class ProfileSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

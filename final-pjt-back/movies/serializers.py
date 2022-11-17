from rest_framework import serializers
from .models import Movie, Nowplaying

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('__all__')
        # exceptions = ('actors, like_users, genres')

class NowMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nowplaying
        fields = ('__all__')
        # exceptions = ('actors, like_users, genres')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('FK',)



# class ArticleSerializer(serializers.ModelSerializer):
#     comment_set = CommentSerializer(many=True, read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     username = serializers.CharField(source='user.username', read_only=True)

#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = ('user', )



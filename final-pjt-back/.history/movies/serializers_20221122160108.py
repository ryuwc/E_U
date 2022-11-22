from rest_framework import serializers
from movies.models import Movie, Nowplaying, Review

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


# 상세 영화 전체 리뷰 조회(GET)
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')
        read_only_fields = ('user', 'movie',)
        # 작성 불요 (read_only_fields)

# 상세 리뷰 조회(GET)
class ReviewSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # 상세 리뷰에 대한 모든 코멘트 조회
    class Meta:
        model = Review
        fields = ('__all__')
        read_only_fields = ('user', 'movie',)
        # 작성 불요 (read_only_fields)

class MovieSerializer(serializers.ModelSerializer):
    
    review_set = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('FK',)


# 영화에 대한 리뷰 작성(POST) 2022.11.19 류원창 수정
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'created_at', 'content', 'user', 'rank', 'good_user', 'bad_user',)
        read_only_fields = ('id', 'created_at', 'good_user', 'bad_user')
        # 작성 불요 (read_only_fields)


# 전체 위시리스트 조회(GET)
class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')
        # exceptions = ('actors, like_users, genres')   




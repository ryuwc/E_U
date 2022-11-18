from rest_framework import serializers
from .models import Movie, Nowplaying, Review

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


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    
    review_set = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('FK',)






from django import forms
from .models import Movie, Review


class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        # fields = ('title', 'content', 'image',)
        # exclude = ('title',)
        exclude = ('user',)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('movie', 'user',)
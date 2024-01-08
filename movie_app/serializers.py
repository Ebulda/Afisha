from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class MovieReviewSerializer(serializers.ModelSerializer):
    review_str_movie = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'title review_str_movie'.split()


    def get_review_str_movie(self,movie):
        texts = [review.text  for review in movie.review.all()]
        star = [review.stars for review in movie.review.all()]
        return texts, star




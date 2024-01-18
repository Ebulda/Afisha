from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=220)
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, min_length=2)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(min_value=1)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise  ValidationError('Director does not exist')
        return director_id

    class Meta:
        model = Movie
        fields = 'title description duration director_id'.split()


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    movie_id = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise  ValidationError('Movie does not exist')
        return movie_id
    class Meta:
        model = Review
        fields = 'text stars movie_id'.split()



class MovieReviewSerializer(serializers.ModelSerializer):
    review_str_movie = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'title review_str_movie'.split()


    def get_review_str_movie(self,movie):
        texts = [review.text  for review in movie.review.all()]
        star = [review.stars for review in movie.review.all()]
        return texts, star



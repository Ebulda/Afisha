from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

@api_view(['GET'])
def director_list_api_view(request):
    directors  = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return   Response(data={'error': 'Director not found'},
                          status=status.HTTP_404_NOT_FOUND)
    serialiser = DirectorSerializer(director)
    return Response(data=serialiser.data)


@api_view(['GET'])
def movies_list_api_view(request):
    movies  = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return   Response(data={'error': 'Movie not found'},
                          status=status.HTTP_404_NOT_FOUND)
    serialiser = MovieSerializer(movie)
    return Response(data=serialiser.data)


@api_view(['GET'])
def reviews_list_api_view(request):
    reviews  = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return   Response(data={'error': 'Review not found'},
                          status=status.HTTP_404_NOT_FOUND)
    serialiser = ReviewSerializer(review)
    return Response(data=serialiser.data)
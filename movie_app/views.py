from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer

@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors  = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer  =DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return   Response(data={'error': 'Director not found'},
                          status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiser = DirectorSerializer(director)
        return Response(data=serialiser.data)
    elif request.method == 'PUT':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    else:
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
        movies  = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT', 'DELETE'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return   Response(data={'error': 'Movie not found'},
                          status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiser = MovieSerializer(movie)
        return Response(data=serialiser.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews  = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return   Response(data={'error': 'Review not found'},
                          status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiser = ReviewSerializer(review)
        return Response(data=serialiser.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
    else:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def movies_reviews_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
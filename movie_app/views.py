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
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return  Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)


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
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)
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
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=MovieSerializer(movies).data, status=status.HTTP_201_CREATED)


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
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data)
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
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        reviews = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        return Response(data=ReviewSerializer(reviews).data, status=status.HTTP_201_CREATED)


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
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(data=ReviewSerializer(review).data)
    else:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def movies_reviews_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewSerializer(movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
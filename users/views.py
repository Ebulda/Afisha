from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterValidateSerializer, AuthorizeValidateSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def register_api_view(request):
    serializer = RegisterValidateSerializer(data=request.data)
    serializer.is_valid()
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    User.objects.create_user(username=username, password=password,is_active=True)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorize_api_view(request):
    serializer = AuthorizeValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=403, data={'error': 'User credential error!'})
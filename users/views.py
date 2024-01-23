from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterValidateSerializer, AuthorizeValidateSerializer, UserConfirmationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import UserConfirmation
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
import random


@api_view(['POST'])
def register_api_view(request):
    serializer = RegisterValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user =User.objects.create_user(**serializer.validated_data,is_active=False)

    code = random.randint(100000, 999999)
    from_email = settings.DEFAULT_FROM_EMAIL
    email = user.email

    if email:
        send_mail(
            subject='Here is your activation code',
            message=str(code),
            from_email=from_email,
            recipient_list=[email],
            fail_silently=False,
        )
    else:
        print("Email is not defined.")

    confirmation = UserConfirmation.objects.create(user=user, code=code)
    return Response({'status': 'User registered',  'data': serializer.data},
                    status=status.HTTP_201_CREATED)



@api_view(['POST'])
def authorize_api_view(request):
    serializer = AuthorizeValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=403, data={'error': 'User credential error!'})


@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = UserConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('code')
    confirmation = get_object_or_404(UserConfirmation, code=code)
    user = confirmation.user
    user.is_active = True
    user.save()
    print(confirmation)
    confirmation.delete()
    return Response({'status': 'User activated'}, status=status.HTTP_200_OK)

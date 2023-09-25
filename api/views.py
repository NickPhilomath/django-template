from django.shortcuts import render
from djoser.serializers import UserSerializer, UserCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def ping_pong(request):
    return Response('pong!', status=status.HTTP_200_OK)
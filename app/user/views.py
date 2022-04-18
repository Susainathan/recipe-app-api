from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, AuthTokenSerializer


class UserCreateView(generics.CreateAPIView):
    """View for creat user"""
    serializer_class = UserSerializer


class CreateToken(ObtainAuthToken):
    """Creata a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
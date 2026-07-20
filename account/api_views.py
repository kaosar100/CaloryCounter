from rest_framework import generics, permissions
from .serializers import SignupSerializer


class SignupAPIView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
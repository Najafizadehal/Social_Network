from django.contrib.auth import get_user_model
from rest_framework import generics
from .Serializer import RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.object.all
    serializers_class = RegisterSerializer
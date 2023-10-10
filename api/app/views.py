from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.app.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que aceita os usuários serem visualizados ou editados.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que aceita os grupos serem visualizados ou editados.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

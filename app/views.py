from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from django.http import HttpRequest

from .models import User
from .serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]


def register(req: HttpRequest):
    template = 'registration.html'
    context = {}
    return render(req, template, context)


def login(req: HttpRequest):
    template = 'login.html'
    context = {}
    return render(req, template, context)

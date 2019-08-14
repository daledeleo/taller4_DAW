from django.shortcuts import render
from .models import *
from .permissions import *
from .serializers import *
from rest_framework import permissions,viewsets

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAdminUserOrReadOnly]


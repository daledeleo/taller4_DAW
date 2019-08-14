from .models import *
from rest_framework import serializers

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
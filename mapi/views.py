from django.shortcuts import render

from rest_framework import viewsets

from .serializers import CompradoresSerializer
from .models import Compradores


class CompradoresViewSet(viewsets.ModelViewSet):
    queryset = Compradores.objects.all().order_by('name')
    serializer_class = CompradoresSerializer

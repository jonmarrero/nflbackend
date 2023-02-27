from django.shortcuts import render
from .models import Nfl
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NflSerializer
# Create your views here.

class NflViewSet(viewsets.ModelViewSet):
    queryset = Nfl.objects.all()
    serializer_class = NflSerializer
    permission_classes = [permissions.AllowAny]

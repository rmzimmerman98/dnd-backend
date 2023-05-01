from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import InitiativeSerializer
from .models import Initiative

class InitiativeList(generics.ListCreateAPIView):
    queryset = Initiative.objects.all().order_by('-initiative')
    serializer_class = InitiativeSerializer

class InitiativeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Initiative.objects.all().order_by('-initiative')
    serializer_class = InitiativeSerializer
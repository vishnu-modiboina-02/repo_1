from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CgargerSerializer
from .models import charger
from rest_framework import viewsets

# Create your views here.
def phone(request):
    return HttpResponse("Welcome")

class ChargerModelViewSet(viewsets.ModelViewSet):
    queryset = charger.objects.all()
    serializer_class = CgargerSerializer








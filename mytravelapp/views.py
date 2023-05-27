from django.shortcuts import render
from .models import Destination

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render
from .models import Animal

def index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/home.html', {'animals': animals})
from django.shortcuts import render
from .models import Team
from django.http import HttpResponse

# Create your views here.
def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def serivces(request):
    return render(request, 'pages/serivces.html')

def contact(request):
    return render(request, 'pages/contact.html')
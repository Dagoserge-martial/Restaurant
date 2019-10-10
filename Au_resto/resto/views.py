from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    #special = Specialite.objects.filter(titre=special)
    special = Specialite.objects.filter(statut=True)
    data = {
        #'specialite': specialite,
        'special': special,
    }
    return render(request, 'pages/index.html', data)

def Menu(request):
    return render(request, 'pages/menu.html')

def Team(request):
    return render(request, 'pages/team.html')

def About(request):
    return render(request, 'pages/about.html')

def Special(request):
    return render(request, 'pages/special-dishes.html')

def Reservation(request):
    return render(request, 'pages/reservation.html')


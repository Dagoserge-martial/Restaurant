from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'pages/index.html' )

def Menu(request):
    return render(request, 'pages/menu.html')

def Team(request):
    return render(request, 'pages/team.html')

def About(request):
    return render(request, 'pages/about.html')

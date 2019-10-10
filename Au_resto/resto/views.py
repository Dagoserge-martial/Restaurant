from django.shortcuts import render
from .models import *
from mainConf.models import *
from master.models import Team

# Create your views here.

def Home(request):
    #special = Specialite.objects.filter(titre=special)
    special = Specialite.objects.filter(statut=True)
    plat = Plat.objects.filter(statut=True)
    platSpec = Plat.objects.filter(isSpecial=True)
    service = Service.objects.filter(statut=True)
    #master = Team.objects.filter(statut=True)[:1].get()
    data = {
        #'specialite': specialite,
        'special': special,
        'plat': plat,
        'platSpec': platSpec,
        'service': service,
        #'menus': menus,
        #'master': master,
    }
    return render(request, 'pages/index.html', data)

def Menu(request):
    special = Specialite.objects.filter(statut=True)
    plat = Plat.objects.filter(statut=True)
    platSpec = Plat.objects.filter(isSpecial=True)
    service = Service.objects.filter(statut=True)
    data = {
        #'specialite': specialite,
        'special': special,
        'plat': plat,
        'platSpec': platSpec,
        'service': service,
        #'menus': menus,
        #'master': master,
    }
    return render(request, 'pages/menu.html', data)

def Team(request):
    return render(request, 'pages/team.html')

def About(request):
    return render(request, 'pages/about.html')

def Special(request):
    return render(request, 'pages/special-dishes.html')

def Reservation(request):
    isSave=False
    myName=request.POST.get('name')
    myEmail=request.POST.get('email')
    myPhone=request.POST.get('phone')
    myDate=request.POST.get('date')
    myTime=request.POST.get('time')
    myPerson=request.POST.get('person')
    myPlace=request.POST.get('place')
    #message=request.POST.get('message')
    print(myName,myEmail,myPhone,myDate,myTime,myPerson,myPlace)
    if request.method =='POST':
        try:
            newRdv=Reservation(name = myname, email = myEmail, phone = myPhone, date = myDate,time = myTime,place_number=myPerson,place=myPlace)
            newRdv.save()
            #newRdv.Reservation.place =place
            isSave=True
            print('Redevous enregistré !')
        except:
            isSave=False
            print('Erreur d\'enregistrement ')
        

    return render(request, 'pages/reservation.html')


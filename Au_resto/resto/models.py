from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField

# Create your models here.

class Service(models.Model):
    nom = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Specialite(models.Model):
    titre = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Menu(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='serviceMenu')
    jour = models.CharField(max_length=255)
    position = models.PositiveIntegerField()

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.jour

class Plat(models.Model):
    specialite = models.ForeignKey(Specialite, on_delete = models.CASCADE, related_name='platspecial')
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE, related_name='platcateg')
    menu = models.ManyToManyField(Menu, related_name='platMenu')
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    prix = models.IntegerField()
    image_menu = models.ImageField(upload_to='plat', blank=True)
    image_special = models.ImageField(upload_to='plat', blank=True)

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Place(models.Model):
    name=models.CharField(max_length=255)

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE,primary_key=True,related_name='placeReservable')
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    time=models.CharField(max_length=255)
    person_number = models.IntegerField()

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

#python manage.py admin_generator resto >> resto/admin.py
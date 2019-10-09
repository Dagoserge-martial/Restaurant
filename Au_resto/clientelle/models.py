from django.db import models

# Create your models here.

class Temoignage(models.Model):
    nom = models.CharField(max_length=160)
    commentaire = models.TextField()
    job = models.CharField(max_length=255)
    entreprise = models.CharField(max_length=255, blank=True)

    statut = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'

class Newsletter(models.Model):
    email = models.EmailField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return self.email


from django.db import models

# Create your models here.
class Team(models.Model):
    nom = models.CharField(max_length=255)
    fontion=models.CharField(max_length=255)
    image = models.ImageField(upload_to='MasterChef/', default='useravatar.png')
    fb_link=models.URLField(blank=True)
    tw_link=models.URLField(blank=True)
    g_link=models.URLField(blank=True)
    insta_link=models.URLField(blank=True)

from django.db import models
from django.utils.translation import ugettext as _
from django.db.models import SmallIntegerField
# Create your models here.

class Conf(models.Model):
    titre=models.CharField(max_length=255)
    logo = models.ImageField(blank=True, upload_to='img')
    video = models.FileField(blank=True, upload_to='video')

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Service(models.Model):
    titre=models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

DAY_OF_THE_WEEK = {
        '1' : _(u'Monday'),
        '2' : _(u'Tuesday'),
        '3' : _(u'Wednesday'),
        '4' : _(u'Thursday'),
        '5' : _(u'Friday'),
        '6' : _(u'Saturday'),
        '7' : _(u'Sunday'),
        
    }

class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1
        super(DayOfTheWeekField,self).__init__(*args, **kwargs)
         
    class Meta:
        
        abstract = True


class Timemodels(models.Model):
    
    statut = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
      
    class Meta:
        abstract = True
           
class Heure_Travail(Timemodels):
    
    # TODO: Define fields here
    jour = DayOfTheWeekField(unique="True")
    ferme = models.BooleanField(default=False)
    heure_debut = models.TimeField(blank=True)
    heure_fin = models.TimeField(blank=True)
    class Meta:
        verbose_name = "Heure_Travail"
        verbose_name_plural = "Heure_Travails"

    def __str__(self):
        
        return '{}  {} - {}'.format(self.jour,self.heure_debut,self.heure_fin)

class Social(Timemodels):
    # TODO: Define fields here
    choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
    name = models.CharField(max_length=100,choices=choice)

    @property
    def font(self):
        
        if self.name == 'FB':
            font = 'fab fa-facebook-f'
        elif self.name == 'TW':
            font ='fab fa-twitter'
        elif self.name == 'INS':
            font ='fab fa-instagram'
        elif self.name == 'GOO':
            font ='fab fa-google-plus-g'
        return font
    class Meta:
            
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    def __str__(self):
            
        return '{}'.format(self.name)

class About(Timemodels):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='img',)

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.titre

class Image_slide(Timemodels):
    image = models.ImageField(upload_to='img',)



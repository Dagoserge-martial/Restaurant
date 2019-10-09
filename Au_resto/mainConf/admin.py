# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ConfAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'logo',
        'video',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'logo',
        'video',
        'statut',
        'date_add',
        'date_upd',
    )


class ServiceAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'icon', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'icon',
        'statut',
        'date_add',
        'date_upd',
    )


class Heure_TravailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'jour',
        'ferme',
        'heure_debut',
        'heure_fin',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'ferme',
        'id',
        'statut',
        'date_add',
        'date_update',
        'jour',
        'ferme',
        'heure_debut',
        'heure_fin',
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'date_add', 'date_update', 'name')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'name',
    )
    search_fields = ('name',)


class AboutAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'statut',
        'date_add',
        'date_update',
        'titre',
        'description',
        'image',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'titre',
        'description',
        'image',
    )


class Image_slideAdmin(admin.ModelAdmin):

    list_display = ('id', 'statut', 'date_add', 'date_update', 'image')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'statut',
        'date_add',
        'date_update',
        'image',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Conf, ConfAdmin)
_register(models.Service, ServiceAdmin)
_register(models.Heure_Travail, Heure_TravailAdmin)
_register(models.Social, SocialAdmin)
_register(models.About, AboutAdmin)
_register(models.Image_slide, Image_slideAdmin)

from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ServiceAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'statut',
        'date_add',
        'date_upd',
    )


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'statut',
        'date_add',
        'date_upd',
    )


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'statut',
        'date_add',
        'date_upd',
    )


class MenuAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'service',
        'jour',
        'position',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'service',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'service',
        'jour',
        'position',
        'statut',
        'date_add',
        'date_upd',
    )


class PlatAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'specialite',
        'categorie',
        'titre',
        'description',
        'prix',
        'image_menu',
        'image_special',
        'isSpecial',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'specialite',
        'categorie',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'specialite',
        'categorie',
        'titre',
        'description',
        'prix',
        'image_menu',
        'image_special',
        'isSpecial',
        'statut',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('menu',)


class PlaceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'name',
        'statut',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'place',
        'name',
        'email',
        'phone',
        'date',
        'time',
        'person_number',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'place',
        'statut',
        'date_add',
        'date_upd',
        'place',
        'name',
        'email',
        'phone',
        'date',
        'time',
        'person_number',
        'statut',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Service, ServiceAdmin)
_register(models.Specialite, SpecialiteAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Plat, PlatAdmin)
_register(models.Place, PlaceAdmin)
_register(models.Reservation, ReservationAdmin)

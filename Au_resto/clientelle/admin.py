# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TemoignageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'commentaire',
        'job',
        'entreprise',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'nom',
        'commentaire',
        'job',
        'entreprise',
        'statut',
        'date_add',
        'date_update',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'email',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Temoignage, TemoignageAdmin)
_register(models.Newsletter, NewsletterAdmin)

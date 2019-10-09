# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TeamAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'fontion',
        'image',
        'fb_link',
        'tw_link',
        'g_link',
        'insta_link',
    )
    list_filter = (
        'id',
        'nom',
        'fontion',
        'image',
        'fb_link',
        'tw_link',
        'g_link',
        'insta_link',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Team, TeamAdmin)

"""le_resto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

from rest_framework.routers import DefaultRouter
from .apiviews import ServiceViewSet, SpecialiteViewSet, CategorieViewSet, MenuViewSet, PlatViewSet,PlaceViewSet, ReservationViewSet

router = DefaultRouter()
router.register('service', ServiceViewSet, base_name='serviceMenu')
router.register('specialite', SpecialiteViewSet, base_name='platspecial')
router.register('categorie', CategorieViewSet, base_name='categorie')
router.register('menuapi', MenuViewSet, base_name='menu')
router.register('platapi', PlatViewSet, base_name='plat')
router.register('placeapi', PlaceViewSet, base_name='place')
router.register('reservationapi', ReservationViewSet, base_name='reservation')


urlpatterns = [
    path('resto', views.Home ,name='index'),
    path('menu', views.Menu ,name='menu'),
    path('team', views.Team ,name='team'),
    path('about', views.About ,name='about'),
]

urlpatterns += router.urls
from rest_framework import serializers

from .models import Service, Specialite, Categorie, Menu, Plat, Place, Reservation
from drf_dynamic_fields import DynamicFieldsMixin

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    placeReservable = ReservationSerializer(many=True, required=False)
    class Meta:
        model = Place
        fields = '__all__'

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    platMenu = PlatSerializer(many=True, required=False)    
    class Meta:
        model = Menu
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    platcateg = PlatSerializer(many=True, required=False) 
    class Meta:
        model = Categorie
        fields = '__all__'

class SpecialiteSerializer(serializers.ModelSerializer):
    platspecial = PlatSerializer(many=True, required=False) 
    class Meta:
        model = Specialite
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    serviceMenu = MenuSerializer(many=True, required=False) 
    class Meta:
        model = Service
        fields = '__all__'  
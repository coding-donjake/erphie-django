from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Country, Province, City, Module, Privilege
from .serializers import CountrySerializer, ProvinceSerializer, CitySerializer, ModuleSerializer, PrivilegeSerializer

# Create your views here.
@api_view(['GET'])
def get_countries(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_provinces(request):
    provinces = Province.objects.all()
    serializer = ProvinceSerializer(provinces, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_cities(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_modules(request):
    modules = Module.objects.all()
    serializer = ModuleSerializer(modules, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_privileges(request):
    privileges = Privilege.objects.all()
    serializer = PrivilegeSerializer(privileges, many=True)
    
    return Response(serializer.data)

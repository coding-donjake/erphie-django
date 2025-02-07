from rest_framework import serializers
from .models import Country, Province, City, Module, Privilege

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'a2', 'a3', 'num', 'status', 'created_at', 'updated_at', 'removed_at']

class ProvinceSerializer(serializers.ModelSerializer):
    country = CountrySerializer()  # Nested serializer to include country details

    class Meta:
        model = Province
        fields = ['id', 'name', 'status', 'country', 'created_at', 'updated_at', 'removed_at']

class CitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()  # Nested serializer to include province details

    class Meta:
        model = City
        fields = ['id', 'name', 'status', 'province', 'created_at', 'updated_at', 'removed_at']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'name', 'status', 'created_at', 'updated_at', 'removed_at']

class PrivilegeSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()  # Nested serializer to include module details

    class Meta:
        model = Privilege
        fields = ['id', 'name', 'status', 'module', 'created_at', 'updated_at', 'removed_at']

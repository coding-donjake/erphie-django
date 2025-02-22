from rest_framework import serializers
from .models import User, Account, Email, Simcard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'suffix', 'gender', 'birth_date'] 
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'status', 'user', 'deactivated_at', 'suspended_at'] 
        
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'username', 'domain_name', 'status', 'account'] 
        
class SimcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simcard
        fields = ['id', 'idc', 'number', 'status', 'account'] 

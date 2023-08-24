from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    """
    account serializer
    """
    
    class Meta:
        """ 
        the fields needed in the account serializer
        """
        model = Account
        fields = ['first_name','last_name','username','email','password','role','address','phone_number']
        
    def create(self, validated_data):
        try:
            print(validated_data)
            account = Account.objects.create(**validated_data)
            return account
        
        except Exception as _e:
            return _e 
        
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
        extrakwargs={'password':{'write_only':True}}
        
    def create(self, validated_data):
       
        account = Account.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            address=validated_data['address'],
            phone_number=validated_data['phone_number'],
            # is_staff=None,
            # is_active=False
            
            
        )
        account.set_password(validated_data['password'])
        return account
        
        
from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """
    account serializer
    """

    class Meta:
        """
        the fields needed in the account serializer
        """

        model = Account
        # fields = "__all__"
        fields =[]
        extra_kwargs = {'passwords':{'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        account = Account.objects.create_user(password=password,**validated_data)
        return account
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_fields = ['first_name','last_name', 'username','address','role','phone_number','email',]
        representation= {field:getattr(instance,field)for field in get_fields}
        return representation

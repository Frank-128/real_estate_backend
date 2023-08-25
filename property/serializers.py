from rest_framework import serializers
from .models import PropertyCategories, PropertyTypes,PropertyAttributes,Property,Attributes


class CategorySerializer(serializers.ModelSerializer):
    """
    property category
    """

    class Meta:
        model = PropertyCategories
        fields = '__all__'

    def create(self, validated_data):
        return PropertyCategories.objects.create(**validated_data)


class PropertyTypeSerializer(serializers.ModelSerializer):
    """
    property type serializer
    """

    class Meta:
        model = PropertyTypes
        fields = "__all__"

    def create(self, validated_data):
        return PropertyTypes.objects.create(**validated_data)


class AttributeSerializer(serializers.ModelSerializer):
    
    """ 
    attribute serializer
    """
    
    class Meta:
        model = Attributes
        fields = '__all__'
        
    def create(self,validated_data):
        return Attributes.objects.create(**validated_data)
    
    
class PropertySerializer(serializers.ModelSerializer):
    """ 
    property serializer
    """
    
    class Meta:
        model = Property
        fields ='__all__'
        
    def create(self,validated_data):
        return Property.objects.create(**validated_data)
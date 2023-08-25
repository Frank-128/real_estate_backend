from rest_framework.views import APIView
from .serializers import CategorySerializer, PropertyTypeSerializer, AttributeSerializer, PropertySerializer
from rest_framework.response import Response
from rest_framework import status
from .models import PropertyTypes, PropertyCategories, PropertyAttributes, Property,Attributes
from django.http import Http404
from django.shortcuts import get_object_or_404


class PropertyCategoryAPI(APIView):
    """
    create a new category or post a new one
    """

    def get(self, request, format=None):
        categories = PropertyCategories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        category = request.data
        serializer = CategorySerializer(data=category)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyCategoryDetailAPI(APIView):
    """
    get , update or delete a category
    """

    def get_object(self, pk):
        try:
            category = get_object_or_404(PropertyCategories, pk=pk)
            return category
        except Http404 as exc:
            raise Http404("Category not found") from exc

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response("category deleted", status=status.HTTP_204_NO_CONTENT)


class PropertyTypeList(APIView):
    """
    get all the properties or create a new property
    """

    def get(self, request, format=None):
        properties = PropertyTypes.objects.all()
        serializer = PropertyTypeSerializer(properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PropertyTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyTypeDetail(APIView):
    """
    get a property type, update or delete
    """

    def get_object(self, pk):
        try:
            property_type = get_object_or_404(PropertyTypes, pk=pk)
            return property_type
        except Http404 as exc:
            raise Http404("Property type not found") from exc

    def get(self, request, pk, format=None):
        property_type = self.get_object(pk)
        serializer = PropertyTypeSerializer(property_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        property_type = self.get_object(pk)
        serializer = PropertyTypeSerializer(property_type, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        property_type = self.get_object(pk)
        property_type.delete()
        return Response("property deleted", status=status.HTTP_204_NO_CONTENT)


class AttributeList(APIView):
    
    """ 
    get all attributes or create an attribute
    """
    
    def get(self, request, format=None):
        attributes = Attributes.objects.all()
        serializers = AttributeSerializer(attributes, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = AttributeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class AttributeDetail(APIView):
    """ 
    get , update or delete and attribut
    """
    
    def get_object(self,pk):
        try:
            attribute = get_object_or_404(Attributes,pk=pk)
            return attribute
        except Http404 as exc:
            raise Http404 from exc
        
    def get(self,request,pk,format=None):
        attribute = self.get_object(pk)
        serializer = AttributeSerializer(attribute)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        attribute = self.get_object(pk)
        
        serializer = AttributeSerializer(attribute,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,pk,format=None):
        attribte = self.get_object(pk)
        attribte.delete()
        
        return Response("attribute deleted successfully",status=status.HTTP_204_NO_CONTENT)
    
        
class PropertyList(APIView):
    """ 
    create a new property or get all properties
    """
    
    def get(self,request,format=None):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PropertyDetail(APIView):
    """ 
    get a property, update or delete the property
    """
    
    def get_object(self,pk):
        try:
            property = get_object_or_404(Property,pk=pk)
            return property
        except Http404 as exc:
            raise Http404 from exc
    
    def get(self,request,pk,format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        property = self.get_object(pk)
        property.delete()
        return Response("property deleted successfully",status=status.HTTP_204_NO_CONTENT)
        
    
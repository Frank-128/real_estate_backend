# from django.db import models
# from accounts.models import Account

# """
# The property category i.e residential and commercial
# """


# class PropertyCategories(models.Model):
#     category_name = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = "property_categories"
#         # ordering = ['created_at']
#         indexes = [
#             models.Index(fields=['category_name'])
#         ]

#     def __str__(self):
#         return self.category_name


# """
#  The types of property eg. house,mansion,villa,office
# """


# class PropertyTypes(models.Model):
#     category = models.ForeignKey(
#         PropertyCategories, on_delete=models.CASCADE, verbose_name="Property Category"
#     )
#     type_name = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = "property_types"
#         # ordering = ['created_at']
#         indexes = [
#             models.Index(fields=['type_name'])
#         ]

#     def __str__(self):
#         return self.type_name


# """
#  attributes of the property
# """


# class Attributes(models.Model):
#     attribute_name = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = "attributes"
#         ordering = ['created_at']
#         indexes = [
#             models.Index(fields=['attribute_name'])
#         ]

#     def __str__(self):
#         return self.attribute_name


# """
#  Address of the Property
# """


# class Address(models.Model):
    # ##region = models.CharField(max_length=15)
#     district = models.CharField(max_length=30)
#     street = models.CharField(max_length=30)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(null=True, blank=True)

#     class Meta:
#         db_table = "property_address"
#         ordering = ['created_at']
#         indexes = [
#             models.Index(fields=['region', 'district', 'street'])
#         ]

#     def __str__(self):
#         return self.region


# """
# Pictures Models
# """


# class PropertyPictures(models.Model):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="user picture")
#     property_picture = models.ImageField(
#         upload_to="property_pictures", height_field=40, width_field=50, null=True
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(null=True, blank=True)

#     class Meta:
#         db_table = "property_pictures"
#         ordering = ["created_at"]

#     def __str__(self):
#         return self.created_at


# """
#  Properties Model
# """


# class Property(models.Model):
#     user = models.ForeignKey(
#         Account, on_delete=models.CASCADE, verbose_name="property owner"
#     )
#     type = models.ForeignKey(
#         PropertyTypes, on_delete=models.CASCADE, verbose_name="property type"
#     )
#     category = models.ForeignKey(
#         PropertyCategories, on_delete=models.CASCADE, verbose_name="property category"
#     )
#     address = models.ForeignKey(
#         Address, on_delete=models.CASCADE, verbose_name="property address"
#     )
#     price = models.FloatField()
#     estate_name = models.CharField(max_length=255)
#     conditions = models.CharField(max_length=255, null=True)
#     utilities = models.CharField(max_length=255, null=True)
#     description = models.TextField(max_length=500)
#     pictures = models.ForeignKey(PropertyPictures, on_delete=models.CASCADE, verbose_name="property picture")
#     is_for_sale = models.BooleanField(
#         default=False
#     )
#     status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=False)

#     class Meta:
#         db_table = "properties"
#         ordering = ['created_at']
#         indexes = [
#             models.Index(fields=['user', 'address'])
#         ]

#     def __str__(self):
#         return self.estate_name


# """
#  Attributes of the specific property
# """


# class PropertyAttributes(models.Model):
#     property = models.ForeignKey(
#         Property, on_delete=models.CASCADE, verbose_name="Property Name"
#     )
#     attribute = models.ForeignKey(
#         Attributes, on_delete=models.CASCADE, verbose_name="Property Attribute"
#     )
#     value = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=False)

#     class Meta:
#         db_table = "property_attributes"
#         ordering = ['created_at']
#         indexes = [
#             models.Index(fields=['attribute'])
#         ]

#     def __str__(self):
#         return f'{self.property.estate_name}'

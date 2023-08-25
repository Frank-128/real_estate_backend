from datetime import datetime
from django.db import models
from accounts.models import Account


class PropertyCategories(models.Model):

    """
    The property category i.e residential and commercial
    """

    category_name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "property_categories"
        ordering = ["created_at"]
        indexes = [models.Index(fields=["category_name"])]

    def __str__(self):
        return f"{self.category_name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.updated_at = None

        else:
            self.updated_at = datetime.now()
        super().save(*args, **kwargs)


class PropertyTypes(models.Model):

    """
    The different types of a property
    """

    category = models.ForeignKey(
        PropertyCategories, on_delete=models.CASCADE, verbose_name="Property Category"
    )
    type_name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "property_types"
        # ordering = ['created_at']
        indexes = [models.Index(fields=["type_name"])]

    def save(self, *args, **kwargs):
        if not self.pk:
            self.updated_at = None
        else:
            self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type_name}"

    objects = models.Manager()


class Attributes(models.Model):

    """
    attributes of the property
    """

    attribute_name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "attributes"
        ordering = ["created_at"]
        indexes = [models.Index(fields=["attribute_name"])]

    def __str__(self):
        return f"{self.attribute_name}"

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.updated_at = None

        else:
            self.updated_at = datetime.now()
        super().save(*args, **kwargs)


class Address(models.Model):
    """
    Address of the Property
    """

    region = models.CharField(max_length=15)
    district = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "property_address"
        ordering = ["created_at"]
        indexes = [models.Index(fields=["region", "district", "street"])]

    def __str__(self):
        return f"{self.region}"

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.updated_at = None

        else:
            self.updated_at = datetime.now()
        super().save(*args, **kwargs)


class PropertyPictures(models.Model):
    """
    Pictures Models
    """

    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, verbose_name="user picture"
    )
    property_picture = models.ImageField(
        upload_to="property_pictures", height_field=40, width_field=50, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "property_pictures"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.created_at}"

    objects = models.Manager()


class Property(models.Model):

    """
    Properties Model
    """

    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, verbose_name="property owner"
    )
    type = models.ForeignKey(
        PropertyTypes, on_delete=models.CASCADE, verbose_name="property type"
    )
    category = models.ForeignKey(
        PropertyCategories, on_delete=models.CASCADE, verbose_name="property category"
    )
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="property address"
    )
    price = models.FloatField()
    estate_name = models.CharField(max_length=255)
    conditions = models.CharField(max_length=255, null=True)
    utilities = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=500)
    pictures = models.ForeignKey(
        PropertyPictures, on_delete=models.CASCADE, verbose_name="property picture",
    )
    is_for_sale = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "properties"
        ordering = ["created_at"]
        indexes = [models.Index(fields=["user", "address"])]

    def __str__(self):
        return f"{self.estate_name}"

    objects = models.Manager()


class PropertyAttributes(models.Model):
    """
    Attributes of the specific property
    """

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, verbose_name="Property Name"
    )
    attribute = models.ForeignKey(
        Attributes, on_delete=models.CASCADE, verbose_name="Property Attribute"
    )
    value = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False)

    class Meta:
        db_table = "property_attributes"
        ordering = ["created_at"]
        indexes = [models.Index(fields=["attribute"])]

    def __str__(self):
        return f"{self.property}"

    objects = models.Manager()

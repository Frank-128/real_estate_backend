from django.db import models
from accounts.models import Account
from property.models import Property



class Order(models.Model):
    """

    The order class for tracking the interactions
    between the property owner and the client

    """

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, verbose_name="property id"
    )

    property_owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="user id",
        related_name="property_owner",
    )

    client = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="client_order",
        verbose_name="user id",
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "orders"
        indexes = [models.Index(fields=["client", "created_at"])]

    def __str__(self):
        return f"{self.property_owner}"

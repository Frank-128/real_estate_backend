""" 
user messages model
"""
from datetime import datetime
from django.db import models
from accounts.models import Account


class Message(models.Model):

    """
    The message model for the messaging interactions between the property owner and the client
    """

    sender = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="sender id",
        related_name="sender_id",
    )
    receiver = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="receiver id",
        related_name="receiver_id",
    )
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        """
        this is the inner class of the model defining the table name and the indexing
        """

        db_table = "users_messages"
        indexes = [models.Index(fields=["sender"])]

    def __str__(self):
        return f"{self.sender} - {self.receiver}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.updated_at = None
        else:
            self.updated_at = datetime.now()
        super().save(*args, **kwargs)

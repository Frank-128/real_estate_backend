from django.db import models

from accounts.models import Account

""" 
The message model for the messaging interactions between the property owner and the client 
"""


class Messages(models.Model):
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
    message = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "users_messages"
        indexes = [
            models.Index(fields=['sender'])
        ]

    def __str__(self):
        return f"{self.sender} - {self.receiver}"

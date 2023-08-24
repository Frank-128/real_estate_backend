from django.contrib.auth.models import AbstractUser
from django.db import models

"""
The user model subclassing all the AbstractUser class for easy user authentication
"""


class Account(AbstractUser):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=20)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", height_field=40, width_field=50, null=True
    )
    role = models.CharField(max_length=255)
    updated_at = models.DateTimeField()
    # is_staff = None
    # is_active = None

    class Meta:
        db_table = 'accounts'
        indexes = [
            models.Index(fields=['username'])
        ]

    def __str__(self):
        return self.username

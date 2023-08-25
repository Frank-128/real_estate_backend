from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):

    """
    The user model subclassing all the AbstractUser class for easy user authentication
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=20)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", height_field=40, width_field=50, null=True
    )
    role = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # is_staff = None
    # is_active = None

    class Meta:
        db_table = "accounts"

        indexes = [models.Index(fields=["username"])]

    def __str__(self):
        return f'{self.username}'

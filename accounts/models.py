

from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    This class is defining the method create_user which is amking the instance of the user in data with hashing
    password and normalizing the email.
    """
    def create_user(self, email, password, **extra_fields):
        """ 
        This method is normalizing email and hashing the password
        """
        if not email:
            raise ValueError("The email field must set")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
        

class Account(AbstractBaseUser):

    """
    The user model subclassing all the AbstractUser class for easy user authentication.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=20)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", null=True , blank=True
    )
    role = models.CharField(max_length=255)
    updated_at = models.DateTimeField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    
    


    class Meta:
        """
        this is the inner class meta describing the table name and the indexes
        
        """
        db_table = "accounts"

        indexes = [models.Index(fields=["username"])]

    def __str__(self):
        return f'{self.username}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.updated_at = None
        else:
            self.updated_at = datetime.now()
        super().save(*args, **kwargs)
        

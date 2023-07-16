from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('user must contain the email id')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password=None):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_active=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    objects=UserManager()
    
    def get_full_name(self):
        return self.name
    def __str__(self):
        return self.email




class Item(models.Model):
    name=models.CharField(max_length=255)
    original_price=models.IntegerField()
    discount_price=models.IntegerField(blank=True)
    image=models.ImageField(upload_to='media',blank=True)
    stock=models.IntegerField(blank=True)
    description=models.TextField()
    def __str__(self):
        return self.name
    

    








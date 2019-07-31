from django.db import models
from django.contrib.auth.models import (AbstractUser,PermissionsMixin)
from rest_framework import permissions



class User(AbstractUser,PermissionsMixin,models.Model):

    """
    MyUser models used for the authentication process and it contains basic
    fields.
    Inherit : AbstractBaseUser, PermissionMixin

    """

    email=models.EmailField('email',max_length= 50,unique = True, blank= False)

    username= models.CharField('username',max_length= 70, unique = True, blank = False)

    is_superuser = models.BooleanField(default=False)

    password = models.CharField('password', max_length= 500, blank= False)

    USERNAME_FIELD='username'
    EMAIL_FIELD='email'
    
    class Meta:
        #renaming database table
        db_table = '_user'

    
    def __str__(self):
        return self.username

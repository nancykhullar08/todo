from django.db import models
from django.contrib.auth.models import (AbstractUser)
from rest_framework import permissions



class User(AbstractUser):

    """
    MyUser models used for the authentication process and it contains basic
    fields.
    Inherit : AbstractUser

    """

    email=models.EmailField('email',max_length= 50,unique = True, blank= False)

    username= models.CharField('username',max_length= 70, unique = True, blank = False)


    USERNAME_FIELD='username'
    EMAIL_FIELD='email'
    
    
    
    class Meta:
        #renaming database table
        db_table = '_user'

    
    def __str__(self):
        return self.username

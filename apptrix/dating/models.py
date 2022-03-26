from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager




class User(AbstractBaseUser):
    CHOOSE_SEX = [('female', 'female'),('male', 'male')]
    name = models.CharField(db_index=True, max_length=255)
    surname = models.CharField(db_index=True, max_length=255)
    sex = models.CharField(choices = CHOOSE_SEX, max_length=6)
    mail = models.EmailField(db_index=True, unique=True)
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    password = models.CharField(max_length=10)



    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.surname

    



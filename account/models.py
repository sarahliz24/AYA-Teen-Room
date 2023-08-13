from django.db import models
from django.contrib.auth.models import AbstractUser

""" class TeenUser(AbstractUser):
    '''
    Custom user model to collect required data from user
    at sign-up
    '''
    username = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name="Display Name")
    medical_id = models.IntegerField(blank=True, null=True, unique=True)
    email = models.EmailField(max_length=50, blank=True, null=True, unique=True, verbose_name="Email")
    date_of_birth = models.DateField(blank=True, null=True) """


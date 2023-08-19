from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinLengthValidator, int_list_validator


""" class TeenUser(AbstractUser):
    '''
    Custom user model to collect required data from user
    at sign-up
    '''
    username = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name="Display Name")
    medical_id = models.IntegerField(blank=True, null=True, unique=True)
    email = models.EmailField(max_length=50, blank=True, null=True, unique=True, verbose_name="Email")
    date_of_birth = models.DateField(blank=True, null=True) """


class TeenUserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank=False, null=True,
                                     help_text='Format: 1900/12/31')
    # blank = False forces medical ID to be completed on form, but allows empty value in DB table (so no errors when profile view created but not yet filled out)
    # https://stackoverflow.com/questions/57131043/how-to-make-integer-field-fixed-to-ten-numbers-output-in-models
    medical_id = models.CharField(blank=False, null=True,
                                     unique=True,
                                     help_text='Required: this is a 7 digit number found on your wristband',
                                     max_length=7, 
                                     validators=[int_list_validator(sep=''),MinLengthValidator(7),])
    fname = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}: Your Profile'

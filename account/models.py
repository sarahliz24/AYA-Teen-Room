from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, int_list_validator


class TeenUserProfile(models.Model):
    '''
    User Profile model
    
    How to fix medical_id length from:
    https://stackoverflow.com/questions/57131043/how-to-make-integer-field-fixed-to-ten-numbers-output-in-models
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    date_of_birth = models.DateField(blank=False, null=True,
                                     help_text='Enter date as: mm/dd/yyyy')
    medical_id = models.CharField(blank=False,
                                  null=True,
                                  unique=True,
                                  help_text="Required: 7 digit number "
                                  "on your wristband",
                                  max_length=7,
                                  validators=[
                                   int_list_validator(sep=''),
                                   MinLengthValidator(7)])
    fname = models.CharField(max_length=20,
                             blank=True,
                             null=True,
                             help_text='Optional',
                             verbose_name="first name")

    def __str__(self):
        return f'{self.user.username}: Your Profile'

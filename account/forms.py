from django import forms
from django.contrib.auth.models import User
from .models import TeenUserProfile


""" class FormLoggingIn(forms.Form):
    '''
    Log in form
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) """


class UserSignUp(forms.ModelForm):
    '''
    User sign up form
    '''
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='Enter password again',
                                      widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password_repeat(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_repeat']:
            raise forms.ValidationError('Your passwords are not the same!')
        return cd['password_repeat']


class EditUser(forms.ModelForm):
    '''
    Form to edit user details
    '''
    class Meta:
        model = User
        fields = ['username', 'email']


class EditTeenUserProfile(forms.ModelForm):
    class Meta:
        model = TeenUserProfile
        fields = ['date_of_birth', 'medical_id', 'fname']

from django import forms
from django.contrib.auth.models import User


class FormLoggingIn(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserSignUp(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='Enter password again',             widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password_repeat(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_repeat']:
            raise forms.VaildationError('Your passwords are not the same!')
        return cd['password_repeat']
from django import forms

class FormLoggingIn(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
from django import forms

class FormLoggingIn(forms.Form):
    username = forms.Charfield()
    password = forms.Charfield(widget=forms.PasswordInput)
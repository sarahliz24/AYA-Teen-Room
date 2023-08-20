from django import forms
# from django.contrib.auth.models import User
from .models import FeedbackReply

class ReplyForm(forms.ModelForm):
    class Meta:
        model = FeedbackReply
        fields = ['author', 'content']

from django import forms
# from django.contrib.auth.models import User
from .models import Feedback, FeedbackReply


class FeedbackSubmission(forms.ModelForm):
    '''
    Creates a form for user to submit feedback.
    Based on Feedback model. 
    '''
    class Meta:
        model = Feedback
        fields = [
           'title', 'author',
            'content', 'room'
        ]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = FeedbackReply
        fields = ['author', 'content']

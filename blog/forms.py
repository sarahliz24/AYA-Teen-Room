from django import forms
# from django.contrib.auth.models import User
from .models import FeedbackPost, FeedbackComment


class FeedbackSubmission(forms.ModelForm):
    '''
    Creates a form for user to submit feedback.
    Based on FeedbackPost model. 
    '''
    class Meta:
        model = FeedbackPost
        fields = [
           'title', 
            'content', 'room'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = FeedbackComment
        fields = ['content']

from django import forms
from .models import FeedbackPost, FeedbackComment


class FeedbackSubmission(forms.ModelForm):
    '''
    Form for user to submit feedback.
    Based on FeedbackPost model.
    '''
    class Meta:
        model = FeedbackPost
        fields = ['title',
                  'content',
                  'room'
                  ]


class CommentForm(forms.ModelForm):
    '''
    Form for comments on feedback.
    Based on FeedbackComment model.
    '''
    class Meta:
        model = FeedbackComment
        fields = ['content']

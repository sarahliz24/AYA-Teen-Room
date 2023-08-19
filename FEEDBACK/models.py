from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ApprovalManager(models.Manager):
    '''
    Custom model manager for posts set to OK for display in feed
    '''
    det get_queryset(self):
    return super().get_queryset.filter(feedback_approval.FeedbackApproval.OK)


class Feedback(models.Model):
    '''
    Docstring goes here
    '''
    class FeedbackApproval(models.TextChoices):
        PENDING = 'PD', 'Pending'
        OK = 'OK', 'Okay'
    

    class Room(models.TextChoices):
            CHI = 'CHI', 'Crumlin'
            SJH = 'SJH', 'St James'
            CUH = 'CUH', 'Cork'
            GUH = 'GUH', 'Galway'


    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='feedback_post')
    content = models.TextField()
    show_feedback = models.TextField(max_length=500)
    published = models.DateTimeField(default=timezone.now)
    feedback_made = models.DateTimeField(auto_now_add=True)
    feedback_updated = models.DateTimeField(auto_now=True)
    feedback_approval = models.CharField(max_length=2,
                                        choices=FeedbackApproval.choices,
                                        default=FeedbackApproval.PENDING)
    room = models.CharField(max_length=3, choices=Room.choices,
                             default=Room.CHI,
                             help_text='Choose the room your feedback is for')
    

objects = models.Manager()
approval = ApprovalManager()

    class Meta:
        '''
        Order feedback posts by most recent date first in
        production mode (?doesn't work in SQL?)
        '''
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-spublished']),
        ]


    def __str__(self):
        return self.title
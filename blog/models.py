from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class ApprovalManager(models.Manager):
    '''
    Custom model manager for posts set to OK for display in feed
    '''
    def get_queryset(self):
        return super().get_queryset().filter(feedback_approval=FeedbackPost.FeedbackApproval.OK)


class FeedbackPost(models.Model):
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
    show_feedback = models.TextField(max_length=500, default='empty')
    published = models.DateTimeField(default=timezone.now)
    feedback_made = models.DateTimeField(auto_now_add=True)
    feedback_updated = models.DateTimeField(auto_now=True)
    feedback_approval = models.CharField(max_length=2,
                                        choices=FeedbackApproval.choices,
                                        default=FeedbackApproval.OK)
    room = models.CharField(max_length=3, choices=Room.choices,
                             default=Room.CHI,
                             help_text='Choose the room your feedback is for')
    

    objects = models.Manager()
    approved = ApprovalManager()

    class Meta:
        '''
        Order feedback posts by most recent date first in
        production mode (?doesn't work in SQL?)
        '''
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published']),
        ]


    def __str__(self):
        return self.title

    # https://www.kodnito.com/posts/slugify-urls-django/
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    
    def get_absolute_url(self):
        return reverse('blog/feedback_detail', args=[self.id])


class FeedbackComment(models.Model):
    feedback_post = models.ForeignKey(FeedbackPost, on_delete=models.CASCADE,
                                related_name="comments")
    author = models.CharField(max_length=20)
    content = models.TextField()
    comment_made = models.DateTimeField(auto_now_add=True)
    comment_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    allowed = models.BooleanField(default=True) # allows setting to False to turn off reply if required

    class Meta():
        ordering = ['comment_made']
        indexes = [models.Index(fields=['comment_made']),]

    def __str__(self):
        return f'Reply by AYA team member: {self.author}'
from django.contrib import admin
from .models import Feedback, FeedbackReply


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'room', 'feedback_approval']
    list_filter = ['author',  'room', 'feedback_approval', 'feedback_made']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)} # auto-fills slug based on title
    raw_id_fields = ['author']  # widget to search for author in admin view
    date_hierachy = 'published'
    ordering = ['feedback_approval', 'published']


@admin.register(FeedbackReply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'reply_made', 'allowed',]
    list_filter = ['allowed', 'reply_made', 'reply_updated']
    search_fields = ['author', 'content']

from django.contrib import admin
from .models import FeedbackPost, FeedbackComment


@admin.register(FeedbackPost)
class FeedbackPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'room', 'feedback_approval']
    list_filter = ['author',  'room', 'feedback_approval', 'feedback_made']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)} # auto-fills slug based on title
    raw_id_fields = ['author']  # widget to search for author in admin view
    date_hierachy = 'published'
    ordering = ['feedback_approval', 'published']


@admin.register(FeedbackComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'comment_made', 'allowed',]
    list_filter = ['allowed', 'comment_made', 'comment_updated']
    search_fields = ['author', 'content']

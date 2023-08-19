from django.contrib import admin
from .models import Feedback

# admin.site.register(Feedback)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'room', 'feedback_approval']
    list_filter = ['author',  'room', 'feedback_approval', 'feedback_made']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)} # auto-fills slug based on title
    raw_id_fields = ['author']  # widget to search for author in admin view
    date_hierachy = 'show_feedback'
    ordering = ['feedback_approval', 'show_feedback']
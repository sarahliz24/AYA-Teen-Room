from django.contrib import admin
from .models import TeenUserProfile

@admin.register(TeenUserProfile)
class TeenUserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'medical_id', 'fname']
    raw_id_fields = ['user']


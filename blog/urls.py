from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('feedback_submission/', views.feedback_submission, 
          name='feedback_submission'),
    path('<int:id>/', views.feedback_detail, name='feedback_detail'),
    path('<int:feedback_id>/reply/', views.post_reply, name='post_reply'),
    path('<int:feedback_id>/feedback_edit/', views.feedback_edit, 
         name='feedback_edit'),
    path('<int:reply_id>/reply_edit/', views.reply_edit, name='reply_edit'),
    path('<int:feedback_id>/delete_feedback/', views.delete_feedback, 
         name='delete_feedback'),
    path('<int:feedback_id>/delete_reply/int:id>/', views.delete_reply, 
         name='delete_reply'),
]

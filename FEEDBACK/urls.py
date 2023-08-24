from django.urls import path
from . import views

app_name = 'FEEDBACK'

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('feedback_submission/', views.feedback_submission, name='feedback_submission'),
    # path('', views.FeedbackListView.as_view(), name='feedback_list'),
    path('<int:id>/', views.feedback_detail, name='feedback_detail'),
    path('<int:feedback_id>/reply/', views.post_reply, name='post_reply'),
    # path('feedback-detail/', views.feedback_detail, name='feedback_detail'),
    path('<int:feedback_id>/feedback_edit/', views.feedback_edit, name='feedback_edit'),
      path('<int:reply_id>/reply_edit/', views.reply_edit, name='reply_edit'),
]
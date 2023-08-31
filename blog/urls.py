from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
     path('about/', views.about, name='about'),

     path('', views.feedback_list, name='feedback_list'),

     path('feedback_submission/', views.feedback_submission, 
          name='feedback_submission'),

     path('<slug>/', views.feedback_detail, name='feedback_detail'),

     path('<slug>/feedback_edit/', views.feedback_edit, 
         name='feedback_edit'),
    
     path('<slug>/delete_feedback/', views.delete_feedback, 
         name='delete_feedback'),

     # path('comment/', views.comment, name='comment'),
]

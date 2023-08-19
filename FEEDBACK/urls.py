from django.urls import path
from . import views

app_name = 'FEEDBACK'

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('<int:id>/', views.feedback_detail, name='feedback_detail'),
]
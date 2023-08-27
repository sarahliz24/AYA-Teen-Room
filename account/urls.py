from django.urls import path
from django.contrib.auth import views as auth_views
from FEEDBACK.views import feedback_list, feedback_detail
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('feedback/', feedback_list, name='feedback'),
    # path('feedback_detail/', views.feedback_detail, name='feedback_detail'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.ProfileEdit, name='edit'),
    path('password-change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

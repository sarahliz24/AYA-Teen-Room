from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# from .views import signup

urlpatterns = [
    # path('login/', views.user_login, name='login')

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('', views.dashboard, name="dashboard"),
    path('feedback/', views.feedback, name='feedback'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.ProfileEdit, name='edit'),

    # path('signup/', signup.as_view(), name='signup'),
    path('password-change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

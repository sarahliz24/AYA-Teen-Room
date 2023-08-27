"""AYA_TEEN_ROOM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from FEEDBACK.views import (
    home_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('FEEDBACK/', include('FEEDBACK.urls', namespace='FEEDBACK')),
    # path('feedback/', include('feedback.urls', namespace='feedback')),
    path('account/', include('account.urls')),
    
# path('registration/', include('templates/registration/signup.html'))
# path('signup/', signup.view, include('account/signup.html'))
]

"""
URL configuration for aflafitnes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout"),
     path('contact',views.contact,name="contact"),
     path('join',views.entroll,name="entroll"),
     path('profile',views.profile,name="profile"),
      path('gallery',views.gallery,name="gallery"),
      path('attendance',views.attendance,name="attendance"),
       path('data',views.data,name="data"),
       path('award',views.award,name="award"),
       path('about',views.about,name="about"),
    
]

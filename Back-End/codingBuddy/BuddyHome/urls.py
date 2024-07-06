"""MAC URL Configuration

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
# from django.contrib import admin
from unicodedata import name
from django import urls
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.index, name="BuddyHome"),
    # path('Login',views.Loginuser,name="LoginUser"),
    # path('Register',views.Registeruser,name="RegisterUSer"),
    # path('viewsome',views.getData,name="getdata"),
    # path('addsome',views.addItem,name="adddata"),
    # path('registeruser',views.RegisterUser,name="Registeruser"),
    path('', views.index, name="BuddyHome"),
    path('about', views.about, name="about"),
    path('home', views.index, name="home"),
    path('contact', views.contact, name="contact"),
    path('team', views.teamMembers, name="Team"),
    path('login', views.login_user, name="login"),
    path('profile/<int:u_ID>', views.userProfile, name="Profile"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register_user, name="register"),
    path('api/', include('BuddyHome.api.urls')),
    path('chat/', include('chat.urls')),

]

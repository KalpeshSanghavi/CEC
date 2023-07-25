"""CEC1 URL Configuration

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
from django.urls import path
from CECApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.country),
    path('india',views.india),
    path('australia',views.australia),
    path('america',views.america),
    path('gujarat',views.gujarat),
    path('maharastra',views.maharastra),
    path('karnataka',views.karnataka),
    path('gandhinagar',views.gandhinagar),
    path('mumbai',views.mumbai),
    path('bengaluru',views.bengaluru),
    path('newsouthwales',views.newsouthwales),
    path('queensland',views.queensland),
    path('southaustralia',views.southaustralia),
    path('tsamnia',views.tsamnia),
    path('sydney',views.sydney),
    path('brisbane',views.brisbane),
    path('adelaide',views.adelaide),
    path('hobart',views.hobart),
]

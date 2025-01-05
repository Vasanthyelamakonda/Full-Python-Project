"""
URL configuration for Flipcart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tkinter.font import names
from xml.sax.expatreader import version

from django.contrib import admin
from django.urls import path

from Booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.show),
    path('home/',views.home,name='home'),
    path('display/',views.display),
    path('student/',views.stdinfo),
    path('sathyahome/',views.sathyahome),
    path('register/',views.register,name='register'),
    path('login/',views.login , name='login'),
    path('welcome/',views.welcome,name='welcome'),
    path('login2/',views.login2,name='login2'),
    path('home2/',views.home2,name='home2'),
    path('register2/',views.register2,name='register2'),
    path('welcome2/',views.welcome2,name='welcome2'),
    path('invalid/',views.invalid,name='invalid'),
    path('registration/',views.registration,name='registration'),
    path('details/',views.details,name='details'),
    path('salary/',views.salary,name='salary'),
    path('bignumber/',views.big,name='bignumber'),
    path('checkticket/',views.checkticket,name='checkticket'),
    path('studentmarks/',views.studentmarks,name='studentmarks'),
    path('employee/',views.employee,name='employee'),
    path('cal/',views.cal,name='cal'),
    path('money/',views.money,name='money'),
    path('password/',views.password,name='password'),
    path('marks/',views.marks,name='marks'),
    path('register3/',views.register3,name='register3'),
]

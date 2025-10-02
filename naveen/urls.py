from django.contrib import admin
from django.urls import path
from naveen import views


urlpatterns = [
    path("about",views.about, name= 'about'),
    path('about.html', views.about, name='about'),
    path('index.html', views.index, name='naveen'),
    path('', views.index, name='naveen'),
    path('services', views.services, name='services'),
    path('services.html', views.services, name='services'),
    path('contact.html', views.contact, name='contact'),
    path('contact', views.contact, name='contact'),
]





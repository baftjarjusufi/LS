from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('teachers/', views.teachers),
    path('about/', views.about),
    path('contact/', views.contact),
    path('courses/', views.courses),
    path('playlist/', views.playlist),
    path('teacherprofil/', views.teacherprofil),
    path('updateprofil/', views.updateprofil),
    path('watchvideo/', views.watchvideo),
    path('login/', views.login),
    path('register/', views.register),
    
]

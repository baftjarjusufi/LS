from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/home.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def teachers(request):
    return render(request, 'accounts/teachers.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def courses(request):
    return render(request, 'accounts/courses.html')

def playlist(request):
    return render(request, 'accounts/playlist.html')

def teacherprofil(request):
    return render(request, 'accounts/teacherprofil.html')

def updateprofil(request):
    return render(request, 'accounts/updateprofil.html')

def watchvideo(request):
    return render(request, 'accounts/watchvideo.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')






# Create your views here.

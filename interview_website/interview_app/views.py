from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    return render(request, 'interview_app/home.html')
def bijubadhu(request):
    return HttpResponse('BijuBadhu_app!')
def profile(request):

    return render(request, 'interview_app/profile.html')
def explore(request):
    return render(request, 'interview_app/explore.html')
def myexperiences(request):
    return render(request, 'interview_app/experiences.html')
    #return HttpResponse('My Experience')
def bookmarks(request):
    return render(request, 'interview_app/bookmarks.html')
def login(request):

    return render(request, 'interview_app/login.html')

def register(request):
    if request.method=="POST":
        pass
        user_dj=request.POST['username']
        email_dj = request.POST['email']
        password_dj=request.POST['password']
        password2_dj = request.POST['password2']
        #if password_dj==password2_dj:


    else:
        return render(request, 'interview_app/register.html')




# Create your views here.



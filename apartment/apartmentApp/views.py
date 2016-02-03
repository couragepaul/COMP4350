from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import loader


def index(request):
    return render(request,'login.html')
	
def loggedin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect('home')
    return redirect('invalidLogin')

def invalidLogin(request):
    html = "Invalid user credentials"
    return HttpResponse(html)

def home(request):
    if not request.user.is_authenticated():
        return redirect('index')
    html = "Welcome to the Apartment Management Application"
    return HttpResponse(html)


from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    return redirect(invalidLogin)

def logoutUser(request):
    logout(request)
    return redirect(index)

def invalidLogin(request):
    html = "Invalid user credentials"
    return HttpResponse(html)

def home(request):
    return render(request,'home.html')


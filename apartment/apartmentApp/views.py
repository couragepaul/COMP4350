from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from lib.dynamo import Dynamo


def index(request):
    return render(request, 'login.html')


def loggedin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username= username, password= password)
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
    if request.user.is_authenticated():
        user = get_object_or_404(User, username=request.user.username)
        messages = Dynamo.get_messages_by_recipient(user.username)
        if request.user.is_staff:
            return render(request,'createMessage.html', {"message_list": messages})
        else:
            return render(request, 'userMessages.html', {"message_list": messages})
    return redirect(logoutUser)


def createUser(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    if request.POST.get('isStaff', False):
        user.is_staff=True 
        user.save()
    if request.user.is_authenticated():
        return render(request, 'managerSettings.html')
    return redirect(logoutUser)


def deleteUser(request):
    user = User.objects.get(username=request.POST['deleteUsername'])
    user.delete()
    if request.user.is_authenticated():
        return render(request,'home.html')
    return redirect(logoutUser)


def managerSettings(request):
    if request.user.is_authenticated() and request.user.is_staff:
        return render(request,'managerSettings.html')
    return redirect(logoutUser)
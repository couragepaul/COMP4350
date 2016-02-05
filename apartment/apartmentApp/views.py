import boto3
import json
import time

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import dynamo


def index(request):
    return render(request,'login.html')


def loggedin(request):
    username = request.POST['username']
    password = request.POST['password']
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
    return render(request,'home.html')


def createUser(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    return render(request, 'home.html')


def deleteUser(request):
    user = User.objects.get(username=request.POST['username'])
    user.delete()
    return render(request, 'home.html')


def createMessageView(request):
    return render(request,'createMessage.html')


def sendMessage(request):
    try:
        user = User.objects.get(username=str(request.POST['send_to']))
        message = {
            'sender': 'test',
            'recipient': user.username,
            'urgency': int(request.POST['urgency']),
            'content': str(request.POST['message']),
            'timestamp': int(time.time())
        }

        dynamo.Dynamo().send_message(message)

        dynamo.Dynamo().get_message_by_recipient(user.username)

        return redirect(sentMessageView)
    except Exception as e:
        print(e)
        return redirect(errorMessage)


def sentMessageView(request):
    return render(request, 'sentMessage.html')


def errorMessage(request):
    html = "Error creating message"
    return HttpResponse(html)

class userMessages(generic.DetailView):
    context_object_name = 'message_list'
    template_name = 'userMessages.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.args[0])
        return dynamo.Dynamo().get_message_by_recipient(user)


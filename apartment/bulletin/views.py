import time
from django.shortcuts import render

from lib.dynamo import Dynamo

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def sendBulletin(request):
    try:
        bulletin = {
            'sender': 'test',
            'content': str(request.POST['message']),
            'timestamp': int(time.time())
        }

        Dynamo.initialize().send_bulletin(bulletin)
    except Exception as e:
        print("\tERROR\tFailed to send bulletin: " + str(e))
        # return redirect(errorMessage)

def sendComment(request):
    try:
        comment = {
            'sender': 'test',
            'content': str(request.POST('message')),
            'timestamp': int(time.time())
        }

        Dynamo.initialize().send_comment(comment)
    except Exception as e:
        print("\tERROR\tFailed to send bulletin comment: " + str(e))
        # return redirect(errorMessage)


def bulletinBoard(request):
    if request.user.is_authenticated():
        return render(request,'bulletinBoard.html')
    return redirect("../")

def createBulletin(request):
    if request.user.is_authenticated():
        return render(request,'createBulletin.html')
    return redirect("../")

def bulletin(request, bulletin_id):
    if request.user.is_authenticated():
        return render(request,'bulletin.html')
    return redirect("../")



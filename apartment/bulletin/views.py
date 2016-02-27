import time
import ast
from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from lib.dynamo import Dynamo


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def sendBulletin(request):
    try:
        bulletin = {
            'sender': 'test',
            'subject': str(request.POST['subject']),
            'content': str(request.POST['message']),
            'timestamp': int(time.time())
        }

        Dynamo.initialize().send_bulletin(bulletin)
        return redirect(createBulletin)
    except Exception as e:
        print("\tERROR\tFailed to send bulletin: " + str(e))
        return redirect(error_message)

def sendComment(request):
    try:
        bulletinString = request.POST['bulletin']
        bulletin = ast.literal_eval(bulletinString)
        comment = {
            'sender': 'test',
            'content': str(request.POST['message']),
            'bulletin_reference': bulletin['sender'] + ':' + bulletin['timestamp'],
            'timestamp': int(time.time())
        }

        Dynamo.initialize().send_comment(comment)
        comments = Dynamo.get_comments(bulletin['sender'], bulletin['timestamp'])
        for comment in comments:
            comment["timestamp"] = time.strftime("%a, %d %b %Y %H:%M", time.localtime(comment["timestamp"]))
        return render(request, 'bulletin.html', {'bulletin':bulletin, 'comment_list':comments})
    except Exception as e:
        print("\tERROR\tFailed to send bulletin comment: " + str(e))
        return redirect(error_message)


def bulletinBoard(request):
    if request.user.is_authenticated():
        bulletins = Dynamo.get_bulletins()
        for bulletin in bulletins:
            bulletin["timestamp"] = str(bulletin["timestamp"])
        return render(request, 'bulletinBoard.html', {"bulletin_list": bulletins})
    return redirect("../")


def createBulletin(request):
    if request.user.is_authenticated():
        return render(request,'createBulletin.html')
    return redirect("../")


def bulletin(request):
    if request.user.is_authenticated():
        bulletinString = request.POST['bulletin']
        bulletin = ast.literal_eval(bulletinString)
        bulletin['time'] = time.strftime("%a, %d %b %Y %H:%M", time.localtime(int(bulletin["timestamp"])))
        comments = Dynamo.get_comments(bulletin['sender'], bulletin['timestamp'])
        for comment in comments:
            comment["timestamp"] = time.strftime("%a, %d %b %Y %H:%M", time.localtime(comment["timestamp"]))
        return render(request, 'bulletin.html', {'bulletin':bulletin, 'comment_list':comments})
    return redirect("../")

def error_message():
    html = "Error creating message"
    return HttpResponse(html)



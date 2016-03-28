import time
import ast
from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .bulletin import Bulletin
from rest.serializers import BulletinSerializer, CommentSerializer
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


        Dynamo.initialize().send_bulletin(BulletinSerializer(bulletin).data)
        return redirect(bulletinBoard)
    except Exception as e:
        print("\tERROR\tFailed to create bulletin: " + str(e))
        return redirect(error_bulletin)

def sendComment(request):
    try:
        bulletin_reference = request.POST['bulletinSender'] + ':' + request.POST['bulletinTimestamp']


        comment = {
            'sender': 'test',
            'content': str(request.POST['message']),
            'bulletin_reference': bulletin_reference,
            'timestamp': int(time.time())
        }

        Dynamo.initialize().send_comment(comment)
        comments = Dynamo.get_comments(Dynamo.get_bulletin_by_reference(bulletin_reference))

        # for comment in comments:
        #     comment["timestamp"] = time.strftime("%a, %d %b %Y %H:%M", time.localtime(comment["timestamp"]))
        return render(request, 'bulletin.html', {'bulletin': bulletin_reference, 'comment_list':comments})
    except Exception as e:
        print("\tERROR\tFailed to send bulletin comment: " + str(e))
        return redirect(error_comment)


def bulletinBoard(request):
    if request.user.is_authenticated():
        bulletins = Dynamo.get_bulletins()
        return render(request, 'bulletinBoard.html', {"bulletin_list": bulletins})
    return redirect("../")


def createBulletin(request):
    if request.user.is_authenticated():
        return render(request,'createBulletin.html')
    return redirect("../")


def viewBulletin(request):
    if request.user.is_authenticated():
        bulletin = Dynamo.get_bulletin_by_reference(
            request.POST['bulletinSender'] + ':' + request.POST['bulletinTimestamp']
        )

        comments = Dynamo.get_comments(bulletin)
        # for comment in comments:
        #     comment["timestamp"] = time.strftime("%a, %d %b %Y %H:%M", time.localtime(comment["timestamp"]))
        return render(request, 'bulletin.html', {'bulletin': bulletin, 'comment_list': comments})
    return redirect("../")

def error_bulletin():
    html = "Error creating bulletin"
    return HttpResponse(html)

def error_comment():
    html = "Error creating comment"
    return HttpResponse(html)



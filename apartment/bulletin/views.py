import time
import ast
from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .bulletin import Bulletin
from rest.serializers import BulletinSerializer, CommentSerializer
from lib.dynamo import Dynamo


def sendBulletin(request):
    try:
        to_send = Bulletin(
            sender='test',
            subject=str(request.POST['subject']),
            content=str(request.POST['message']),
            timestamp=int(time.time())
        )

        Dynamo.initialize().send_bulletin(BulletinSerializer(to_send).data)
        return redirect(createBulletin)
    except Exception as e:
        print("\tERROR\tFailed to create bulletin: " + str(e))
        return redirect(error_bulletin)

def sendComment(request):
    try:
        bulletinString = request.POST['bulletin']
        bulletin = ast.literal_eval(bulletinString)
        comment = {
            'sender': 'test',
            'content': str(request.POST['message']),
            'bulletin_timestamp': int(bulletin['timestamp']),
            'bulletin_sender': bulletin['sender'],
            'timestamp': int(time.time())
        }

        Dynamo.initialize().send_comment(CommentSerializer(comment).data)
        return redirect(bulletin)
    except Exception as e:
        print("\tERROR\tFailed to send bulletin comment: " + str(e))
        return redirect(error_comment)


def bulletinBoard(request):
    bulletins = Dynamo.get_bulletins()
    for bulletin in bulletins:
            bulletin["timestamp"] = str(bulletin["timestamp"])
    return render(request, 'bulletinBoard.html', {"bulletin_list": bulletins})

def createBulletin(request):
    return render(request, 'createBulletin.html')

def bulletin(request):
    bulletinString = request.POST['bulletin']
    bulletin = ast.literal_eval(bulletinString)
    comments = Dynamo.get_comments(bulletin['sender'], Decimal(bulletin['timestamp']))
    return render(request, 'bulletin.html', {'bulletin':bulletin, 'comment_list':comments})

def error_bulletin():
    html = "Error creating bulletin"
    return HttpResponse(html)

def error_comment():
    html = "Error creating comment"
    return HttpResponse(html)



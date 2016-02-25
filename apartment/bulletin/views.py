import time
import ast
from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse

from lib.dynamo import Dynamo


def sendBulletin(request):
    try:
        bulletin = {
            'sender': 'test',
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
        bulletin = request.POST['bulletin']
        comment = {
            'sender': 'test',
            'content': str(request.POST['message']),
            'bulletin_id': int(bulletin['bulletin_id']),
            'timestamp': int(time.time())
        }

        Dynamo.initialize().send_comment(comment)
        bulletin = request.POST['bulletin']
        return redirect(bulletin(bulletin.bulletin_id))
    except Exception as e:
        print("\tERROR\tFailed to send bulletin comment: " + str(e))
        return redirect(error_message)


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

def error_message():
    html = "Error creating message"
    return HttpResponse(html)



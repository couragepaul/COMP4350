import time
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
        comment = {
            'sender': 'test',
            'content': str(request.POST['message']),
            'timestamp': int(time.time())
        }

        Dynamo.initialize().send_comment(comment)
        bulletin = request.POST['bulletin']
        return redirect(bulletin(bulletin.bulletin_id))
    except Exception as e:
        print("\tERROR\tFailed to send bulletin comment: " + str(e))
        return redirect(error_message)


def bulletinBoard(request):
    return render(request, 'bulletinBoard.html')

def createBulletin(request):
    return render(request, 'createBulletin.html')

def bulletin(request, bulletin_id):
    return render(request, 'bulletin.html')

def error_message():
    html = "Error creating message"
    return HttpResponse(html)



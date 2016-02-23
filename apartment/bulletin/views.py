import time
from django.shortcuts import render

from lib.dynamo import Dynamo


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
    return render(request, 'bulletinBoard.html')

def createBulletin(request):
    return render(request, 'createBulletin.html')

def bulletin(request, bulletin_id):
    return render(request, 'bulletin.html')



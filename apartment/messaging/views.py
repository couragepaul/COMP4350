import time
import ast
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .message import Message
from rest.serializers import MessageSerializer
from lib.dynamo import Dynamo


def create_message_view(request):
    if request.user.is_authenticated():
        user = get_object_or_404(User, username=request.user.username)
        messages = Dynamo.get_messages_by_recipient(user.username)
        if request.user.is_staff:
            return render(request,'createMessage.html', {"message_list": messages})
        else:
            return render(request, 'userMessages.html', {"message_list": messages})
    return redirect("../apartmentApp")


def send_message(request):
    try:
        user = User.objects.get(username=str(request.POST['username'])).username
        to_send = Message(
            sender='test',
            recipient=user,
            urgency=int(request.POST['urgency']),
            content=str(request.POST['message']),
            timestamp=int(time.time()),
            read=False
        )

        Dynamo.initialize().send_message(MessageSerializer(to_send).data)
        Dynamo.get_messages_by_recipient(user)

        return redirect(sent_message_view)
    except Exception as e:
        print("\tERROR\tFailed to create message: " + str(e))
        return redirect(error_message)

def sent_message_view(request):
    if request.user.is_authenticated():
        return render(request,'sentMessage.html')
    return redirect("../apartmentApp")


def error_message(request):
    html = "Error creating message"
    return HttpResponse(html)


def message(request):
    message = dict()
    message['recipient'] = request.POST['messageRecipient']
    message['timestamp'] = int(request.POST['messageTimestamp'])

    message = Dynamo.get_message(message)
    return render(request, 'message.html', {"msg": message})






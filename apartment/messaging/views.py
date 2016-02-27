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
        return render(request,'createMessage.html')
    return redirect("../apartmentApp")


def send_message(request):
    try:
        user = 'test'#User.objects.get(username=str(request.POST['name'])).username
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


def message(request, recipient):
    messageString = request.POST['message']
    message = ast.literal_eval(messageString)
    message['read'] = True
    message['timestamp'] = int(message['timestamp'])
    message['urgency'] = int(message['urgency'])
    del message['time']
    #Dynamo.update_message(message)
    message["timestamp"] = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(message["timestamp"]))
    return render(request, 'message.html', {"msg": message})


class UserMessages(generic.ListView):
    context_object_name = 'message_list'
    template_name = 'userMessages.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.args[0])
        messages = Dynamo.get_messages_by_recipient(user.username)
        for msg in messages:
            msg["time"] = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(msg["timestamp"]))
            msg["timestamp"] = str(msg["timestamp"])
            msg["urgency"] = str(msg["urgency"])
        return messages






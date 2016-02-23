import time

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User

from lib.dynamo import Dynamo


def create_message_view(request):
    return render(request, 'createMessage.html')


def send_message(request):
    try:
        user = User.objects.get(username=str(request.POST['send_to']))
        to_send = {
            'sender': 'test',
            'recipient': user.username,
            'urgency': int(request.POST['urgency']),
            'content': str(request.POST['message']),
            'timestamp': int(time.time()),
            'read': False
        }

        Dynamo.initialize().send_message(to_send)
        Dynamo.get_messages_by_recipient(user.username)

        return redirect(sent_message_view)
    except Exception as e:
        print("\tERROR\tFailed to create message: " + str(e))
        return redirect(error_message)


def sent_message_view(request):
    return render(request, 'sentMessage.html')


def error_message():
    html = "Error creating message"
    return HttpResponse(html)


# def message(request, message_id):
#     get_message = Dynamo.get_message(recipient, )[0]
#     get_message['read'] = True
#     Dynamo.update_message(get_message)
#     get_message["timestamp"] = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(get_message["timestamp"]))
#     return render(request, 'message.html', {"msg": get_message})


class UserMessages(generic.ListView):
    context_object_name = 'message_list'
    template_name = 'userMessages.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.args[0])
        messages = Dynamo.get_message_by_recipient(user.username)
        for msg in messages:
            msg["timestamp"] = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(msg["timestamp"]))
        return messages






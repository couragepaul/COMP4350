import time
import ast
from decimal import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest.serializers import EventSerializer
from lib.dynamo import Dynamo


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def sendEvent(request):
    try:
        event = {
            'sender': 'test',
            'title': str(request.POST['title']),
            'content': str(request.POST['message']),
            'timestamp': int(time.time()),
            'starttime': str(request.POST['starttime']),
            'endtime': str(request.POST['endtime']),
        }


        Dynamo.initialize().send_bulletin(EventSerializer(event).data)
        return redirect(createEvent)
    except Exception as e:
        print("\tERROR\tFailed to create event: " + str(e))
        return redirect(error_event)

def calendar(request):
    if request.user.is_authenticated():
        events = Dynamo.get_events()
        return render(request, 'calendar.html', {"events": events})
    return redirect("../")


def createEvent(request):
    if request.user.is_authenticated():
        return render(request,'createEvent.html')
    return redirect("../")


def viewEvent(request):
    if request.user.is_authenticated():
        event = Dynamo.get_event_by_reference(
            request.POST['EventSender'] + ':' + request.POST['EventTimestamp']
        )

        return render(request, 'event.html', {'event': event})
    return redirect("../")

def error_event():
    html = "Error creating event"
    return HttpResponse(html)

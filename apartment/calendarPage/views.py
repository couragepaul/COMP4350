import time
import datetime
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
        starttime = request.POST['starttime']
        starttime = time.mktime(datetime.datetime.strptime(starttime, "%Y-%m-%dT%H:%M").timetuple())
        endtime = request.POST['endtime']
        endtime = time.mktime(datetime.datetime.strptime(endtime, "%Y-%m-%dT%H:%M").timetuple())
        event = {
            'sender': 'test',
            'title': str(request.POST['title']),
            'content': str(request.POST['message']),
            'location': str(request.POST['location']),
            'timestamp': int(time.time()),
            'starttime': starttime,
            'endtime': endtime,
        }


        Dynamo.initialize().send_event(EventSerializer(event).data)
        return redirect(calendar)
    except Exception as e:
        print("\tERROR\tFailed to create event: " + str(e))
        return redirect(error_event)

def calendar(request):
    #if request.user.is_authenticated():
    eventList = Dynamo.get_events()
    print (dir(eventList[2]))
    return render(request, 'calendar.html', {"eventList": eventList})
    #return redirect("../")


def createEvent(request):
    if request.user.is_authenticated():
        return render(request,'createEvent.html')
    return redirect("../")


def viewEvent(request):
    if request.user.is_authenticated():
        eventList = Dynamo.get_event_by_reference(
            request.POST['EventSender'] + ':' + request.POST['EventTimestamp']
        )

        return render(request, 'viewEvent.html', {'eventList': eventList})
    return redirect("../")

def error_event():
    html = "Error creating event"
    return HttpResponse(html)

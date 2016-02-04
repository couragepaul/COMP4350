from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
import datetime

from .models import Message


def index(request):
    return HttpResponse("Please log in.")

class createMessageView(generic.CreateView):
    model = Message
    fields = ['sent_to', 'message_text', 'urgency']
    template_name = 'apartmentApp/createMessage.html'

def sendMessage(request):
    print request.POST['message']
    try:
        message = request.POST['message']

    except (KeyError, Message.DoesNotExist):
        return render(request, 'apartmentApp/sentMessage.html', {'error_message':'Error in sending message'})

    else:
        message.pub_date = datetime.datetime.now()
        message.save()
        return HttpResponseRedirect(reverse('apartmentApp:sentMessage', args=(message.id,)))


class sentMessageView(generic.DetailView):
    model = Message
    template_name = 'apartmentApp/sentMessage.html'


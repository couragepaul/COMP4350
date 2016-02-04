import boto3
import json
import datetime

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

aws_access_key_id = "AKIAIGLM2CBBY5EOMXYQ"
aws_secret_access_key = "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"

session = boto3.setup_default_session(
	aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key
)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")

table = dynamodb.Table("Message")

def index(request):
    return render(request,'login.html')

def loggedin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect('home')
    return redirect(invalidLogin)

def logoutUser(request):
    logout(request)
    return redirect(index)

def invalidLogin(request):
    html = "Invalid user credentials"
    return HttpResponse(html)

def home(request):
    return render(request,'home.html')

def createUser(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    return render(request, 'home.html')

def deleteUser(request):
    user = User.objects.get(username=request.POST['username'])
    user.delete()
    return render(request, 'home.html')


def createMessageView(request):
    return render(request,'createMessage.html')

def sendMessage(request):
    username = request.POST['send_to']
    message_text = request.POST['message']
    urgency = request.POST['urgency']
    pub_date = datetime.datetime.now()
    try:
        sent_to = User.objects.get(username = username)
        message_id = 1001
        table.put_item(
	        Item={
		        'message_id' : message_id,
		        'timestamp' : pub_date,
		        'content' : {
                    "message_text":message_text,
                    "urgency":urgency,
                    "sent_to":sent_to,
                    "sent_by":"Manager",
                    "has_read":False
                }
	        }
        )
        return redirect(sentMessageView)
    except:
        return redirect(errorMessage)

def sentMessageView(request):
    return render(request, 'sentMessage.html')

def errorMessage(request):
    html = "Error creating message"
    return HttpResponse(html)


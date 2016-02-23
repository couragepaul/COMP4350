from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message
from . import dynamo
import boto3
import datetime

class UserTestCase(TestCase):

    def test_user_create(self):
        name = 'Timmy the Tester'
        user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
        self.assertTrue(User.objects.get(username=name))

    def test_user_create_wrong_format_name(self):
        name = '&*7sdsaidiahu2#~!@#$%^&*()<>'
        user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
        self.assertFlase(User.objects.get(username=name))

    def test_user_create_no_name(self):
        name = ''
        user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
        self.assertFlase(User.objects.get(username=name))

    def test_user_create_wrong_format_email(self):
        name = 'Tommy'
        user = User.objects.create_user(name, 'blahblahdsa.com', 'password')
        self.assertFlase(User.objects.get(username=name))


    def test_user_delete(self):
        name = 'Timmy the Tester'
        user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
        User.objects.get(username=name)
        self.assertTrue(User.objects.get(username=name).delete())

    def test_get_user(self):
        name = 'Timmy the Tester'
        user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
        User.objects.get(username=name)
        self.assertTrue(User.objects.get(username=name))

class MessageTestCase(TestCase):

    def test_message_create(self):
        message_id = 0
        timestamp = datetime.datetime.now()
        message_text = 'Hello, tenant'
        urgency = 1
        sent_to = 'Room1 the Tester'
        sent_by = 'manager'
        has_read = False
        message = Message(message_id=message_id,pub_date=timestamp,message_text=message_text,urgency=urgency,
                          sent_to=sent_to,sent_by=sent_by,has_read=has_read)
        message.save()
        testMessage = Message.objects.get(message_id = message_id)

        self.assertTrue(testMessage.message_id==message_id)
        self.assertTrue(testMessage.message_text==message_text)
        self.assertTrue(testMessage.urgency==urgency)
        self.assertTrue(testMessage.sent_to==sent_to)
        self.assertTrue(testMessage.sent_by==sent_by)
        self.assertTrue(testMessage.has_read==has_read)

    def test_message_create_no_recipient(self):
        message_id = 0
        timestamp = datetime.datetime.now()
        message_text = 'Hello, tenant'
        urgency = 1
        sent_to = ''
        sent_by = 'manager'
        has_read = False
        message = Message(message_id=message_id,pub_date=timestamp,message_text=message_text,urgency=urgency,
                          sent_to=sent_to,sent_by=sent_by,has_read=has_read)
        message.save()
        self.assertFalse(Message.objects.get(message_id = message_id))

    def test_message_create_recipient_not_in_database(self):
        message_id = 0
        timestamp = datetime.datetime.now()
        message_text = 'Hello, tenant'
        urgency = 1
        sent_to = 'djfnjsd'
        sent_by = 'manager'
        has_read = False
        message = Message(message_id=message_id,pub_date=timestamp,message_text=message_text,urgency=urgency,
                          sent_to=sent_to,sent_by=sent_by,has_read=has_read)
        message.save()
        self.assertFalse(Message.objects.get(message_id = message_id))

    def test_message_create_no_message_content(self):
        message_id = 0
        timestamp = datetime.datetime.now()
        message_text = ''
        urgency = 1
        sent_to = 'Room1 the Tester'
        sent_by = 'manager'
        has_read = False
        message = Message(message_id=message_id,pub_date=timestamp,message_text=message_text,urgency=urgency,
                          sent_to=sent_to,sent_by=sent_by,has_read=has_read)
        message.save()
        self.assertFalse(Message.objects.get(message_id = message_id))

    def test_message_mark(self):
        message = dynamo.Dynamo().get_message_by_id(message_id=1000)
        message[0]['read'] = True
        dynamo.Dynamo().update_message(message[0])
        self.assertTrue(dynamo.Dynamo().get_message_by_id(message_id=1000)[0]['read'])

    def test_message_delete(self):
        message_id = 0
        timestamp = datetime.datetime.now()
        message_text = 'Hello, tenant'
        urgency = 1
        sent_to = 'Room1 the Tester'
        sent_by = 'manager'
        has_read = False
        message = Message(message_id=message_id,pub_date=timestamp,message_text=message_text,urgency=urgency,
                          sent_to=sent_to,sent_by=sent_by,has_read=has_read)
        message.save()
        Message.objects.get(message_id = message_id)
        self.assertTrue(Message.objects.get(message_id = message_id).delete())


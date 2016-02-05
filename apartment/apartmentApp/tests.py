from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message
import datetime

class UserTestCase(TestCase):

	def test_user_create(self):
		name = 'Timmy the Tester'
		user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
		self.assertTrue(User.objects.get(username=name))

	def test_user_delete(self):
		name = 'Timmy the Tester'
		user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
		User.objects.get(username=name)
		self.assertTrue(User.objects.get(username=name).delete())

class MessageTestCase(TestCase):

    def test_message_send(self):
        message_id = 1001
        timestamp = datetime.datetime.now()
        message_text = 'Hello, tenant'
        urgency = 1
        sent_to = 'Room1 the Tester'
        sent_by = 'manager'
        has_read = False
        message = Message(message_id=message_id,pub_date=timestamp,message_text=message_text,urgency=urgency,
                          sent_to=sent_to,sent_by=sent_by,has_read=has_read)
        message.save()

        self.assertTrue(Message.objects.get(message_id = message_id))
        self.assertTrue(Message.objects.get(pub_date = timestamp))
        self.assertTrue(Message.objects.get(message_text = message_text))
        self.assertTrue(Message.objects.get(urgency = urgency))
        self.assertTrue(Message.objects.get(sent_to = sent_to))
        self.assertTrue(Message.objects.get(sent_by = sent_by))
        self.assertTrue(Message.objects.get(has_read = has_read))

    def test_message_delete(self):
        message_id = 1001
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
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.models import Message

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

    def test_message_create(self):
        message_id = 0
        timestamp = datetime.datetime.now()
        message_text = 'Hello, tenant'
        urgency = 1
        sent_to = 'Room1 the Tester'
        sent_by = 'manager'
        has_read = False
        message = Message.objects.create_message(message_id,timestamp,message_text,urgency,sent_to,sent_by,has_read)
        self.assertTrue(Message.objects.get(message_id = message_id))

    def test_message_mark(self):
        message = dynamo.Dynamo().get_message_by_id(message_id=0)
        message[0]['read'] = True
        dynamo.Dynamo().update_message(message[0])
        self.assertTrue(Message.objects.get(read=true))

    def test_message_delete(self):
        message_id = 0
        timestamp = datetime.datetime.now()
        message_text = 'Hello, tenant'
        urgency = 1
        sent_to = 'Room1 the Tester'
        sent_by = 'manager'
        has_read = False
        message = Message.objects.create_message(message_id,timestamp,message_text,urgency,sent_to,sent_by,has_read)
        Message.objects.get(message_id = message_id)
        self.assertTrue(Message.objects.get(message_id = message_id).delete())
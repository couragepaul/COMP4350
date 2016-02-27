from django.test import TestCase
import datetime

from apartmentApp.models import Message
from lib.dynamo import Dynamo

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

    def test_message_create_no_urgency_selected(self):
        message_id = 0
        timestamp = datetime.datetime.now()
        message_text = 'Hello, tenant'
        urgency = ''
        sent_to = 'Room1 the Tester'
        sent_by = 'manager'
        has_read = False
        message = Message(message_id=message_id,pub_date=timestamp,message_text=message_text,urgency=urgency,
                          sent_to=sent_to,sent_by=sent_by,has_read=has_read)
        message.save()
        self.assertFalse(Message.objects.get(message_id = message_id))

    def test_message_mark(self):
        message = Dynamo.get_message_by_id(message_id=1000)
        message[0]['read'] = True
        Dynamo.update_message(message[0])
        self.assertTrue(Dynamo.get_message_by_id(message_id=1000)[0]['read'])

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
from django.test import TestCase

# Create your tests here.
import datetime

from calendarPage.event import Event
from lib.dynamo import Dynamo


class CalendarTestCase(TestCase):

    def test_event_create(self):
        sender = "Qing"
        title = "Doing a test"
        location = "EITC2"
        starttime = "2016-03-28;10:30AM"
        endtime = "2016-03-28;11:30AM"
        timestamp = datetime.datetime.now()
        message = "cannot forget"

        event = Event(sender=sender,title=title,location=location,starttime=starttime,
                          endtime=endtime,timestamp=timestamp,message=message)
        event.save()
        testEvent = Event.objects.get(title = title)

        self.assertTrue(testEvent.title==title)
        self.assertTrue(testEvent.sender==sender)
        self.assertTrue(testEvent.location==location)
        self.assertTrue(testEvent.starttime==starttime)
        self.assertTrue(testEvent.endtime==endtime)
        self.assertTrue(testEvent.timestamp==timestamp)
        self.assertTrue(testEvent.message==message)

    def test_create_event_no_title(self):
        sender = "Qing"
        location = "EITC2"
        title = ""
        starttime = "2016-03-28;10:30AM"
        endtime = "2016-03-28;11:30AM"
        timestamp = datetime.datetime.now()
        message = "cannot forget"

        event = Event(sender=sender,location=location,title=title,starttime=starttime,endtime=endtime,timestamp=timestamp,message=message)
        event.save()
        self.assertFalse(Event.objects.get(title = title))

    def test_create_event_no_location(self):
        sender = "Qing"
        title = "Doing a test"
        location = ""
        starttime = "2016-03-28;10:30AM"
        endtime = "2016-03-28;11:30AM"
        timestamp = datetime.datetime.now()
        message = "cannot forget"

        event = Event(sender=sender,title=title,location=location,starttime=starttime,
                          endtime=endtime,timestamp=timestamp,message=message)
        event.save()
        self.assertFalse(Event.objects.get(title = title))

    def test_create_event_no_starttime(self):
        sender = "Qing"
        title = "Doing a test"
        location = "EITC2"
        starttime = ""
        endtime = "2016-03-28;11:30AM"
        timestamp = datetime.datetime.now()
        message = "cannot forget"

        event = Event(sender=sender,title=title,location=location,starttime=starttime,
                          endtime=endtime,timestamp=timestamp,message=message)
        event.save()
        self.assertFalse(Event.objects.get(title = title))

    def test_create_event_no_message(self):
        sender = "Qing"
        title = "Doing a test"
        location = "EITC2"
        starttime = "016-03-28;10:30AM"
        endtime = "2016-03-28;11:30AM"
        timestamp = datetime.datetime.now()
        message = ""

        event = Event(sender=sender,title=title,location=location,starttime=starttime,
                          endtime=endtime,timestamp=timestamp,message=message)
        event.save()
        self.assertFalse(Event.objects.get(title = title))

    def test_create_event_and_delete(self):
        sender = "Qing"
        title = "Doing a test"
        location = "EITC2"
        starttime = "2016-03-28;10:30AM"
        endtime = "2016-03-28;11:30AM"
        timestamp = datetime.datetime.now()
        message = "cannot forget"

        event = Event(sender=sender,title=title,location=location,starttime=starttime,
                          endtime=endtime,timestamp=timestamp,message=message)
        event.save()
        Event.objects.get(title=title)
        self.assertTrue(Event.objects.get(title = title).delete())
from django.conf import settings
import time


class Event(object):
    def __init__(self, *args, **kwargs):
        vals = self.process_args(args, kwargs)

        self.sender = vals['sender']
        self.starttime = vals['starttime']
        self.endtime = vals['endtime']
        self.title = vals['title']
        self.content = vals['content']
        self.timestamp = int(vals['timestamp'])

    def process_args(self, args, kwargs):
        if len(kwargs) == 6:
            return kwargs
        elif len(args) == 1:
            return args[0]
        elif settings.CREATE_STUBS:
            # CREATE A STUB BULLETIN
            return self.create_stub()
        else:
            raise CommentException()

    def create_stub(self):
        return {
            "sender": "StubSender",
            "content": "Stub Comment Body",
            "timestamp": time.time(),
            "starttime": time.time(),
            "endtime": time.time(),
            "title": "Stub Title",
        }


class CommentException(BaseException):
    def __init__(self):
        super(CommentException, self).__init__("Failed to create Event. Please refer to constructor.")
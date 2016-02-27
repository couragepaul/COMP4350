from django.conf import settings
import time


class Comment(object):
    def __init__(self, *args, **kwargs):
        vals = self.process_args(args, kwargs)

        self.sender = vals['sender']
        self.bulletin_reference = vals['bulletin_reference']
        self.content = vals['content']
        self.timestamp = int(vals['timestamp'])

    def process_args(self, args, kwargs):
        if len(kwargs) == 4:
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
            "subject": "Stub Subject"
        }


class CommentException(BaseException):
    def __init__(self):
        super(CommentException, self).__init__("Failed to create Comment. Please refer to constructor.")
from django.conf import settings
import time


class Bulletin(object):
    def __init__(self, *args, **kwargs):
        vals = self.process_args(args, kwargs)

        self.sender = vals['sender']
        self.subject = vals['subject']
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
            raise BulletinException()

    def create_stub(self):
        return {
            "sender": "StubSender",
            "content": "Stub Bulletin Body",
            "timestamp": time.time(),
            "subject": "Stub Subject"
        }

    def get_reference(self):
        return self.sender + ':' + str(self.timestamp)


class BulletinException(BaseException):
    def __init__(self):
        super(BulletinException, self).__init__("Failed to create Bulletin. Please refer to constructor.")
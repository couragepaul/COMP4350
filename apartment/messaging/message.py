from django.conf import settings
import time

class Message(object):
    def __init__(self, *args, **kwargs):
        vals = self.process_args(args, kwargs)

        self.sender = vals['sender']
        self.recipient = vals['recipient']
        self.urgency = int(vals['urgency'])
        self.content = vals['content']
        self.timestamp = int(vals['timestamp'])
        self.read = (vals['read'] == 'True')

    def process_args(self, args, kwargs):
        if len(kwargs) == 6:
            return kwargs
        elif len(args) == 1:
            return args[0]
        elif settings.CREATE_STUBS:
            # CREATE A STUB MESSAGE
            return self.create_stub()
        else:
            raise MessageException()

    def create_stub(self):
        return {
            "sender": "StubSender",
            "recipient": "StubRecipient",
            "urgency": "1",
            "content": "Stub Message Body",
            "timestamp": time.time(),
            "read": "False"
        }


class MessageException(BaseException):
    def __init__(self):
        super(MessageException, self).__init__("Failed to create Message. Please refer to constructor.")
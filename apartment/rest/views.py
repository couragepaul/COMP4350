import time

from rest_framework import viewsets
from rest_framework.response import Response

from rest.serializers import MessageSerializer
from messaging.message import Message
from lib.dynamo import Dynamo


class MessageViewSet(viewsets.ViewSet):
    """
    A ViewSet for sending and retrieving messages.
    """
    def retrieve(self, request, pk=None):
        message_list = Dynamo.get_messages_by_recipient(pk)
        serializer = MessageSerializer(message_list, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            request.data['read'] = 'False'
            request.data['timestamp'] = str(int(time.time()))

            serializer = MessageSerializer(data=request.data)
            serializer.is_valid()

            Dynamo.send_message(serializer.validated_data)
        except Exception as e:
            print(e)
            return Response({
                "Status": "Failure",
                "Data Received": request.data})
        return Response({
            "Status": "Success",
            "Data Received": request.data})


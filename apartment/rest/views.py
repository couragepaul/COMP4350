import time

from rest_framework import viewsets
from rest_framework.response import Response

from rest.serializers import MessageSerializer, BulletinSerializer, CommentSerializer
from messaging.message import Message
from bulletin.bulletin import Bulletin
from bulletin.comment import Comment
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
                "Status": "Fail",
                "Data Received": request.data})
        return Response({
            "Status": "Success",
            "Data Received": request.data})


class BulletinViewSet(viewsets.ViewSet):
    """
    A ViewSet for sending and retrieving bulletins.
    """
    def list(self, request):
        bulletin_list = Dynamo.get_bulletins()
        serializer = BulletinSerializer(bulletin_list, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ViewSet):
    """
    A ViewSet for sending and retrieving comments.
    """
    def retrieve(self, request, pk=None):
        try:
            bulletin = Dynamo.get_bulletin_by_reference(pk.replace('%#A', ':'))
            comment_list = Dynamo.get_comments(bulletin)
            serializer = CommentSerializer(comment_list, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
        return Response({
            'Status': 'Fail',
            'Data Received': request.data
        })
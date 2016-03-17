import time

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from rest.serializers import MessageSerializer, BulletinSerializer, CommentSerializer, EventSerializer
from lib.dynamo import Dynamo


class MessageViewSet(viewsets.ViewSet):
    '''
    A ViewSet for sending and retrieving messages.
    '''
    def retrieve(self, request, pk=None):
        message_list = Dynamo.get_messages_by_recipient(pk)
        serializer = MessageSerializer(message_list, many=True)
        
        if len(serializer.data):
            return Response({
                'Status': 'Success',
                'Response': serializer.data
            })
        return Response({
                'Status': 'Fail',
                'Response': serializer.data
            })

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
                'Status': 'Fail',
                'Received': request.data})
        return Response({
            'Status': 'Success',
            'Received': request.data})

    @list_route(methods=['post'])
    def mark_read(self, request):
        try:
            # To Pass Serializer
            request.data['sender'] = 'a'
            request.data['content'] = 'a'
            request.data['read'] = "False"
            request.data['urgency'] = "1"

            serializer = MessageSerializer(data=request.data)
            serializer.is_valid()

            update_msg = Dynamo.get_message(serializer.validated_data)
            update_msg.read = True

            response = Dynamo.update_message(update_msg)

        except Exception as e:
            print(e)
            return Response({
                'Status': 'Fail',
                'MessageRef': {
                    'recipient': request.data['recipient'],
                    'timestamp': request.data['timestamp']
                }
            })
        return Response({
            'Status': 'Success',
            'MessageRef': {
                'recipient': request.data['recipient'],
                'timestamp': request.data['timestamp']
            }
        })

class BulletinViewSet(viewsets.ViewSet):
    '''
    A ViewSet for sending and retrieving bulletins.
    '''
    def list(self, request):
        bulletin_list = Dynamo.get_bulletins()
        serializer = BulletinSerializer(bulletin_list, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            request.data['timestamp'] = str(int(time.time()))

            serializer = BulletinSerializer(data=request.data)
            serializer.is_valid()

            Dynamo.send_bulletin(serializer.validated_data)
        except Exception as e:
            print(e)
            return Response({
                'Status': 'Fail',
                'Received': request.data})
        return Response({
            'Status': 'Success',
            'Received': request.data})

class CommentViewSet(viewsets.ViewSet):
    '''
    A ViewSet for sending and retrieving comments.
    '''
    def retrieve(self, request, pk=None):
        try:
            bulletin = Dynamo.get_bulletin_by_reference(pk.replace('%#A', ':'))
            comment_list = Dynamo.get_comments(bulletin)
            serializer = CommentSerializer(comment_list, many=True)
        except Exception as e:
            print(e)
            return Response({
                'Status': 'Fail',
                'Received': request.data
            })
        return Response({
            'Status': 'Success',
            'Response': serializer.data})

    def create(self, request):
        try:
            request.data['timestamp'] = str(int(time.time()))

            serializer = CommentSerializer(data=request.data)
            serializer.is_valid()

            Dynamo.send_comment(serializer.validated_data)
        except Exception as e:
            print(e)
            return Response({
                'Status': 'Fail',
                'Received': request.data})
        return Response({
            'Status': 'Success',
            'Received': request.data})

class EventViewSet(viewsets.ViewSet):
    '''
    A ViewSet for sending and retrieving comments.
    '''
    def list(self, request):
        event_list = Dynamo.get_events()
        serializer = EventSerializer(event_list, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            request.data['timestamp'] = str(int(time.time()))

            serializer = EventSerializer(data=request.data)
            serializer.is_valid()

            Dynamo.send_event(serializer.validated_data)
        except Exception as e:
            print(e)
            return Response({
                'Status': 'Fail',
                'Received': request.data})
        return Response({
            'Status': 'Success',
            'Received': request.data})
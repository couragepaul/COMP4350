from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    sender = serializers.CharField(max_length=32)
    recipient = serializers.CharField(max_length=32)
    urgency = serializers.IntegerField()
    content = serializers.CharField(max_length=256)
    timestamp = serializers.IntegerField()
    read = serializers.BooleanField()
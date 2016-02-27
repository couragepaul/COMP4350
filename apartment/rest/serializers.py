from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    sender = serializers.CharField(max_length=32)
    recipient = serializers.CharField(max_length=32)
    urgency = serializers.IntegerField()
    content = serializers.CharField(max_length=256)
    timestamp = serializers.IntegerField()
    read = serializers.BooleanField()


class BulletinSerializer(serializers.Serializer):
    sender = serializers.CharField(max_length=32)
    timestamp = serializers.IntegerField()
    subject = serializers.CharField(max_length=256)
    content = serializers.CharField(max_length=256)


class CommentSerializer(serializers.Serializer):
    bulletin_reference = serializers.CharField(max_length=128)
    timestamp = serializers.IntegerField()
    sender = serializers.CharField(max_length=32)
    content = serializers.CharField(max_length=256)
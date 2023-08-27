from rest_framework import serializers

from user_messages.models import Message


class UserMessageSerializer(serializers.ModelSerializer):
    """
    user_message serializer
    """

    class Meta:
        """
        the fields needed in the message serializer
        """

        model = Message
        fields = "__all__"

    def create(self, validated_data):
        user_message = Message.objects.create(**validated_data)
        return user_message

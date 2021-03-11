from django.contrib.auth.models import User
from rest_framework import serializers
from event_app.models import Event, EventType


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    event_type = EventTypeSerializer()

    class Meta:
        model = Event
        fields = ['info', 'timestamp', 'event_type', ]

    def create(self, validated_data):
        EventType.objects.create(**validated_data['event_type'])
        event_type = EventType.objects.all().last()
        validated_data['event_type'] = event_type

        user_id = self.context['request'].user.id
        user = User.objects.get(pk=user_id)
        validated_data['user'] = user

        event = Event.objects.create(**validated_data)
        return event



from rest_framework import serializers

from .models import Cameras, DogEvents, TrashEvent, SuspiciousObjectEvent, Events, Logs, Settings_API


def validate_camera_count(value):
    Cameras.object.filter(id=value).count()
    if value.count(0):
        raise serializers.ValidationError("Camera not found")
    else:
        return value


def validate_status(value):
    Cameras.objects.filter(status=value)
    if Cameras.objects.filter(status=value):
        raise serializers.ValidationError("Camera not found")
    else:
        return value


def validate_active(value):
    event_active = Cameras.objects.all()
    if value not in event_active:
        raise serializers.ValidationError("Camera not active")
    else:
        return value


def validate_adress(value):
    Cameras.objects.filter(adress=value)
    if Cameras.objects.filter(adress=value):
        raise serializers.ValidationError("there's no camera at that address")
    else:
        return value


def validate_coordinates(value):
    if Cameras.objects.filter(coordinates=value):
        raise serializers.ValidationError("there's no camera at that coordinates")
    else:
        return value


def validate_stream_url(value):
    if Cameras.objects.filter(stream_url=value):
        raise serializers.ValidationError("there's no camera at that stream_url")
    else:
        return value


class CamerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cameras
        fields = '__all__'


def validate_dogs_count(value):
    DogEvents.objects.filter(dogs_count=value)
    if value < 0:
        raise serializers.ValidationError("Dogs count is too low")
    else:
        return value


def validate_person(value):
    DogEvents.objects.filter(distance_to_person=value)
    if value:
        raise serializers.ValidationError("distance")
    elif not value:
        raise serializers.ValidationError("Invalid distance")


def validate_confidance(value):
    DogEvents.objects.filter(confidence=value)
    if DogEvents.objects.filter(confidence=value):
        raise serializers.ValidationError("Invalid confidence")
    elif value < 8:
        raise serializers.ValidationError("Invalid confidence")


class DogsEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogEvents
        fields = '__all__'


def validate_trash_count(value):
    TrashEvent.objects.filter(trash_count=value)
    if TrashEvent.objects.filter(trash_count=value):
        raise serializers.ValidationError("Trash count is too high")
    elif value < 1:
        raise serializers.ValidationError("Trash count is too low")


class TrashEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashEvent
        fields = '__all__'


class SuspiciousObjectEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspiciousObjectEvent
        fields = '__all__'


def validate_priority(value):
    Events.objects.filter(pk=value).count()
    if Events.objects.filter(priority=value):
        raise serializers.ValidationError("Invalid priority")


def validate_status_object(value):
    Events.objects.filter(status=value)
    if Events.objects.filter(status=value):
        raise serializers.ValidationError("Invalid status")


def validate_event(value):
    Events.objects.filter(timestamp=value)
    if Events.objects.filter(timestamp=value):
        raise serializers.ValidationError("Timestamp is required ")


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'

class Settings_APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings_API
        fields = '__all__'


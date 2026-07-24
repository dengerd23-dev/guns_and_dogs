from django.db import models

# Create your models here.
class ServiceSetting(models.Model):
    key = models.TextField()
    value = models.TextField()
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.key}: {self.value}"

class Cameras(models.Model):
    name = models.TextField()
    status = models.BooleanField()
    address = models.CharField(max_length=255)
    stream_id = models.TextField()
    longitude = models.TextField()
    zone_type = models.TextField()
    stream_url = models.TextField()

    def __str__(self):
        return f"{self.address}: {self.status}: {self.name}"

class DogEvents(models.Model):
    status = models.BooleanField    ()
    created_at = models.DateTimeField(auto_now_add=True)
    camera_id = models.TextField()
    dogs_count = models.IntegerField()
    persson_detected = models.IntegerField()
    distance_to_person = models.IntegerField()
    is_pack = models.FloatField()
    is_dangerous = models.FloatField()
    confidence = models.FloatField()
    detected_at = models.FloatField()

    def __str__(self):
        return f" {self.status}: {self.created_at}"

class Events(models.Model):
    camera_id = models.TextField()
    event_type = models.TextField()
    priority = models.TextField()
    confidence = models.FloatField()
    status = models.BooleanField()
    source_type = models.TextField()
    source_event_id = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f" {self.status}"

class PublicSafetyEvent(models.Model):
    camera_id = models.TextField()
    event_type = models.TextField()
    priority = models.TextField()
    confidence = models.FloatField()
    metadata = models.TextField()
    is_send_to_core = models.IntegerField()
    sent_at = models.DateTimeField()

    def __str__(self):
        return f" {self.event_type}: {self.priority}"

class TrashEvent(models.Model):
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    count_trashed = models.IntegerField()

    def __str__(self):
        return f" {self.status}"

class SuspiciousObjectEvent(models.Model):
    camera_id = models.TextField()
    object_type = models.TextField()
    standing_time_minutes = models.IntegerField()
    people_nearby = models.IntegerField()
    is_suspicious = models.FloatField()
    confidence = models.IntegerField()
    priority = models.TextField()
    detected_at = models.DateTimeField()

    def __str__(self):
        return f" {self.object_type}: {self.standing_time_minutes}"

class LogsEvent(models.Model):
    camera_id = models.TextField()
    event_type = models.TextField()
    priority = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.status}: {self.event_type}: {self.priority}"

class Logs(models.Model):
    camera_id = models.TextField()
    event_type = models.TextField()

    def __str__(self):
        return f"{self.event_type}: {self.camera_id}"

class Settings_API(models.Model):
    count_dogs = models.IntegerField()
    time_object = models.IntegerField()
    cooldown_events = models.IntegerField()
    min_confidence = models.IntegerField()

    def __str__(self):
        return f"{self.count_dogs}: {self.time_object}, {self.cooldown_events}, {self.min_confidence}"

class Priority(models.Model):
    camera_id = models.TextField()
    dogs_count = models.IntegerField(default=0)
    trash_count = models.IntegerField(default=0)
    suspicious_count = models.IntegerField(default=0)
    count_person = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.dogs_count}: {self.trash_count}, {self.suspicious_count}"
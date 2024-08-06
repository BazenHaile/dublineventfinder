# This file defines the database structure for our application
# Each class represents a table in the database

from django.db import models
from django.contrib.auth.models import AbstractUser
from django_cryptography.fields import encrypt
from django.conf import settings
import os

# This class extends the default User model to add custom fields
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='events/images/default.jpg', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    contact_phone = models.CharField(max_length=15, blank=True)
    saved_events = models.ManyToManyField('Event', blank=True, related_name='saved_by_users')

    def __str__(self):
        return self.username

# This class represents an Event in our application

DUBLIN_LOCATIONS = [
    ('DUBLIN_1', 'Dublin 1'),
    ('DUBLIN_2', 'Dublin 2'),
    ('DUBLIN_3', 'Dublin 3'),
    ('DUBLIN_4', 'Dublin 4'),
    ('DUBLIN_5', 'Dublin 5'),
    ('DUBLIN_6', 'Dublin 6'),
    ('DUBLIN_6W', 'Dublin 6W'),
    ('DUBLIN_7', 'Dublin 7'),
    ('DUBLIN_8', 'Dublin 8'),
    ('DUBLIN_9', 'Dublin 9'),
    ('DUBLIN_10', 'Dublin 10'),
    ('DUBLIN_11', 'Dublin 11'),
    ('DUBLIN_12', 'Dublin 12'),
    ('DUBLIN_13', 'Dublin 13'),
    ('DUBLIN_14', 'Dublin 14'),
    ('DUBLIN_15', 'Dublin 15'),
    ('DUBLIN_16', 'Dublin 16'),
    ('DUBLIN_17', 'Dublin 17'),
    ('DUBLIN_18', 'Dublin 18'),
    ('DUBLIN_20', 'Dublin 20'),
    ('DUBLIN_22', 'Dublin 22'),
    ('DUBLIN_24', 'Dublin 24'),
    ('DUN_LAOGHAIRE_RATHDOWN', 'Dún Laoghaire–Rathdown'),
    ('FINGAL', 'Fingal'),
    ('SOUTH_DUBLIN', 'South Dublin'),
]

class Event(models.Model):
    # Basic event details
    name = models.CharField(max_length=100)
    # The description is encrypted for privacy
    description = encrypt(models.TextField())
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=50, choices=DUBLIN_LOCATIONS)
    # Boolean field to indicate if the event requires entrance fee
    entrance = models.BooleanField(default=False)
    # Foreign key relationship: each event is organized by a user
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organized_events')
    address = models.CharField(max_length=255, blank=True)
    # Geographical coordinates of the event
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    # Choices for event status
    STATUS_CHOICES = (
        ('PL', 'Planning'),
        ('OG', 'Ongoing'),
        ('CP', 'Completed'),
        ('CN', 'Cancelled'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PL')
    
    # Choices for event category
    CATEGORY_CHOICES = [
        ('MUSIC', 'Music'),
        ('SPORTS', 'Sports'),
        ('ARTS', 'Arts & Culture'),
        ('FOOD', 'Food & Drink'),
        ('OTHER', 'Other'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')

    def __str__(self):
        # This method defines how the event object is represented as a string
        return self.name

# This class represents a Message in our application
class Message(models.Model):
    # Foreign key relationships: each message has a sender and a receiver
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=100)
    # The body of the message is encrypted for privacy
    body = encrypt(models.TextField())
    # Automatically set when the message is created
    sent_at = models.DateTimeField(auto_now_add=True)
    # Flags to track message status
    read = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def __str__(self):
        # This method defines how the message object is represented as a string
        return f'From {self.sender.username} to {self.receiver.username} - {self.subject}'
    
    
    
class EventApplication(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='event_applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} - {self.event.name}"

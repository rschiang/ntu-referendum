from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models

class Referendum(models.Model):
    number = models.PositiveSmallIntegerField('referendum number', default=0)
    subject = models.CharField(max_length=140)
    description = models.CharField(max_length=210, blank=True)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    starts_on = models.DateTimeField(default=datetime.min)
    ends_on = models.DateTimeField(default=datetime.max)
    enabled = models.BooleanField(default=True)

class Option(models.Model):
    referendum = models.ForeignKey(Referendum)
    number = models.PositiveSmallIntegerField('option number', default=0)
    title = models.CharField(max_length=70)
    subtitle = models.CharField(max_length=140)
    slug = models.SlugField(max_length=32, blank=True)

class Ballot(models.Model):
    referendum = models.ForeignKey(Referendum)
    option = models.ForeignKey(Option, null=True)
    token = models.CharField(max_length=256, unique=True)

class Record(models.Model):
    INVALID = '-'
    VOTED = 'V'
    BLOCKED = 'X'

    STATE_CHOICES = (
        (INVALID, 'invalid'),
        (VOTED, 'voted'),
        (BLOCKED, 'blocked'),
    )

    user = models.ForeignKey(get_user_model())
    referendum = models.ForeignKey(Referendum)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default=INVALID)

import uuid

from django.contrib.auth.models import User
from django.db import models

class Candidate(models.Model):
    WAITING = 0
    VOTING = 1
    APPROVED = 2
    REJECTED = 3
    STATUS_CHOICES = (
        (WAITING, 'Waiting'),
        (VOTING, 'Voting'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    contact_email = models.EmailField()
    users = models.ManyToManyField(User, through='Vote')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    approve = models.NullBooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Photo(models.Model):
    candidate = models.OneToOneField(Candidate, null=True)
    firebase_path = models.CharField(max_length=1024)
    firebase_name = models.CharField(max_length=1024)
    firebase_bucket = models.CharField(max_length=1024)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

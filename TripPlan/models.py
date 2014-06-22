from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
	users = models.ManyToManyField(User)
	name = models.CharField(max_length=255)
	created_datetime = models.DateTimeField(auto_now_add=True)
	edited_datetime = models.DateField(auto_now=True)
	start_date = models.DateField()
	end_date = models.DateField()

class Activity(models.Model):
    trip = models.ForeignKey(Trip)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    source_api = models.CharField(max_length=255)
    api_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField()
    notes = models.TextField()

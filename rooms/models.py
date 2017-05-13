from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Room(models.Model):
 author = models.ForeignKey('auth.User')
 room_title = models.CharField(max_length=50)
 room_location = models.CharField(max_length=50)
 room_description = models.CharField(max_length=300)
 created_date = models.DateTimeField(default=timezone.now)
 pub_date = models.DateTimeField('date published')


 def publish(self):
     self.pub_date = timezone.now()
     self.save()

 def __str__(self):
     return self.room_title

from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible  # only if you need to support Python 2
class Room(models.Model):

 room_title = models.CharField(max_length=50)
 room_location = models.CharField(max_length=50)
 room_description = models.CharField(max_length=300)
 pub_date = models.DateTimeField('date published')


 def __str__(self):
     return self.room_title

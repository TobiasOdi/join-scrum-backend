from django.db import models
from django.conf import settings
from django.db.models.fields import DateField
from datetime import date

# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.IntegerField()
    color = models.CharField(max_length=25)

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    username2 = User.username
    first_name  = User.first_name
    last_name  = User.last_name
    email = User.email

    # OneToOneField stellt die Beziehung zwischen einem Account- und einem User-Objekt her
    
    username = models.CharField(max_length=50, blank=False, default=None)
    first_name = models.CharField(max_length=50, blank=False, default=None)
    last_name = models.CharField(max_length=50, blank=False, default=None)
    email = models.CharField(max_length=50, blank=False, default=None)
    color = models.CharField(max_length=25, blank=False, default=None)
    phone = models.CharField(max_length=25, blank=True, default=None)
    
    def __str__(self):
        return self.user.username
    
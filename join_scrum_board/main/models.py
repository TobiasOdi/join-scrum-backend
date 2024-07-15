from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    # OneToOneField stellt die Beziehung zwischen einem Account- und einem User-Objekt her
    color = models.CharField(max_length=25, blank=False)
    phone = models.CharField(max_length=25, blank=True)
    
    def __str__(self):
        return self.user.username
    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=100, blank=True)
    farm_details = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    description = models.TextField(max_length=255,blank=True,null=True)


    def __str__(self):
        return self.username
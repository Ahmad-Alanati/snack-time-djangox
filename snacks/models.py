from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    purchaser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('snack_list')
    
    class Meta:
        ordering = ['name']
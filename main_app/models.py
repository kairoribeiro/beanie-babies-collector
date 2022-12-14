from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Baby(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    image = CloudinaryField('media')
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('babies_detail', kwargs={'baby_id': self.id})
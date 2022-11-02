from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Contact(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.email

class Blogs(models.Model):
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    title = models.CharField(max_length=600)
    image = models.ImageField()
    content = models.TextField()
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
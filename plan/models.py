from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Friend(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email

class Plan(models.Model):
    friend = models.ManyToManyField(Friend, related_name='friend')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    scheduled_date = models.DateField()

    def __str__(self):
        return self.title
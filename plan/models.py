from django.db import models

# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    scheduled_date = models.DateField()

    def __str__(self):
        return self.title
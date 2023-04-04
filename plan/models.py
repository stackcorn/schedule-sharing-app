from django.db import models
from django.contrib.auth.models import User

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

class Friends(models.Model):

    class Meta:
        verbose_name = '友達リスト'
        verbose_name_plural = '友達リスト'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='友達', related_name = 'friend_friends')

    def __str__(self):
        return f'{self.friend}'
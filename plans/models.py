from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plans(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, # 参照先が削除された場合、参照元のレコードも削除される
        related_name='plans_owner', # related_nameを使うことで逆参照が可能となる
        )
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        )
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __srt__(self):
        return str(self.content) + ' (' + str(self.owner) + ')'
    
    class Meta:
        # 'ordering' must be a tuple or list (even if you want to order by only one field).
        ordering = ('created_at',) # 投稿が古い順に並び替える

class Group(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_owner',
    )
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return '<' + self.group_name + ' (' + str(self.owner) + ')>'
    
class Friend(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='friend_owner',
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + '(group:"' + str(self.group) + '")'
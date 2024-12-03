from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class messages(models.Model):
    body=models.TextField()
    sender=models.ForeignKey(User, on_delete=models.CASCADE)
    receiver=models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    seen=models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    def __str__(self):
        return f"{self.sender} - {self.receiver}: {self.body}"

class friends(models.Model):
    user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)    
    friend=models.ForeignKey(User, related_name='friend', on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)

    def __str__(self):
        return f"{self.user} - {self.friend}"    
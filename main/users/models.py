from django.db import models
import uuid
# Create your models here.
class Profile(models.Model):
    file = models.ImageField(upload_to='uploads/',default="uploads/download.png")
    full_name = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=150,null=True,blank=True)
    address=models.CharField(max_length=500,blank=True,null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    def __str__(self):
        return self.full_name



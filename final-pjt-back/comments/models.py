from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    usernumber = models.IntegerField()

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
   
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(verbose_name='Нравится', default=0)

class Repost(models.Model):
    source = models.ForeignKey(Post, related_name="reposts", on_delete=models.CASCADE)
    destination = models.OneToOneField(Post, related_name="src", on_delete=models.CASCADE)
    text = models.TextField
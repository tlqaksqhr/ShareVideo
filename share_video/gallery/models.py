from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    desc = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

class Comment(models.Model):
    desc = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
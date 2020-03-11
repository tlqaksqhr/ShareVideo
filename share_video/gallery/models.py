from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    desc = models.TextField()
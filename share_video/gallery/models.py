from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    desc = models.TextField()
    write_date = models.DateField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='posts')
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE,related_name='posts')

class Comment(models.Model):
    desc = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    write_date = models.DateField()

class Favorite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='favorites')

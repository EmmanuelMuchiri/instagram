from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome Me!")

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Profile, related_name='comments',on_delete=models.CASCADE)

class Likes(models.Model):
    user = models.ForeignKey(Profile, related_name='mylikes',on_delete=models.CASCADE)

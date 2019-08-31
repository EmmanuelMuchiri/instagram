from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    Name = models.TextField(default="Anonymous")
    profile_picture = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome Me!")

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(Profile, related_name='posts',on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='comments',on_delete=models.CASCADE)

class Likes(models.Model):
    user = models.ForeignKey(Profile, related_name='mylikes',on_delete=models.CASCADE)
    photo = models.ForeignKey(Post, related_name='photolikes',on_delete=models.CASCADE)

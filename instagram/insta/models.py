from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default='profile')
    profile_photo = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Instagram IG!")

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Profile, default='comments', on_delete=models.CASCADE)


class Likes(models.Model):
    user = models.ForeignKey(Profile, default='mylikes', on_delete=models.CASCADE)
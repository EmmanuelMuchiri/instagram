from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='user')
    profile_name = models.TextField(default="Anonymous")
    profile_picture = models.ImageField(upload_to='users/', default='users.jpg')
    bio = models.TextField(default="Hey dear!")


class Image(models.Model):
    image_url = models.ImageField(upload_to = 'images/',blank=True,default="image_url")
    image_name = models.CharField(max_length=30,default="title")
    image_caption =  models.CharField(max_length=30,default="title")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default='profile')
    # comments = models.ManyToManyField(Comment)
    # likes = models.ManyToManyField(Like)
    

class Comment(models.Model):
    text = models.TextField()
    comment = models.ForeignKey(Image, default='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, default='comments',on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(Profile, default='profile',on_delete=models.CASCADE)
    image = models.ForeignKey(Image, default='likes',on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.TextField(default="Anonymous")
    profile_picture = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Instagram!")

class Comment(models.Model):
    text = models.TextField()

class Likes(models.Model):
    text = models.TextField()

class Image(models.Model):
    image_url = models.ImageField(upload_to = 'images/',blank=True,default="image_url")
    image_name = models.CharField(max_length=30,default="title")
    image_caption = models.TextField()
    likes = models.ManyToManyField(Likes)
    comments = models.ManyToManyField(Comment)
    

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length = 70)
    content = models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    #has a one to many relationship
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name= "comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.post} comment by {self.name}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class LikePost(models.Model):
    username = models.CharField(max_length=200)
    post_id = models.IntegerField()
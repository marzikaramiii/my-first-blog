from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=50,unique = True)
    created_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)
    color_label = models.CharField(max_length=50,blank=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
    
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)
    tags = models.ManyToManyField(Tag)
    def publish(self):
        self.publish_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title
    def approved_comment(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text






    





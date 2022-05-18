from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField

# Create your models here.
class Education(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length = 50)
    description = models.TextField()
    
class Contact(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    vemail = models.EmailField()
    phone_no = models.IntegerField()
    message = models.TextField()

    def __str__(self):
     return self.name

class Blog(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    description =  HTMLField()
    title2 = HTMLField()
    poster = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def image_url(self):
        if self.image:
            return self.image.url


    def __str__(self):
        return self.title              


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'comment by {self.name} on {self.post}'

class Register(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    password = models.IntegerField()
    vpassword = models.IntegerField()
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname





from django.db import models
from django.contrib.auth.models import User
import uuid


# django.contrib.auth
# https://docs.djangoproject.com/ja/5.0/ref/contrib/auth/


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        blank=True,
        null=True,
        upload_to="profiles/",
        default="profiles/user-default.png",
    )
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        # 安全のためにstrで変換しておく
        return str(self.user.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return str(self.name)

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL,blank=True, null=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL,blank=True, null=True,related_name="messages")
    name = models.CharField(max_length=200,blank=True, null=True)
    email = models.CharField(max_length=200,blank=True, null=True)
    subject = models.CharField(max_length=200,blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False,null=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    
    def __str__(self) -> str:
        return self.subject
    
    class Meta:
        # 下記のlistのトップの順からソート処理をしていく
        ordering =["is_read","-created"]
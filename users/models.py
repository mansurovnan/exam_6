from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.png" )
    bio = models.TextField(max_length=150, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tel_number = models.CharField( max_length=15,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.username


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    ordering = ['-created_at']


    


    


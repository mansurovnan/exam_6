from django.db import models
from django.conf import settings
from users.models import CustomUser
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="posts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey("categories.Category",on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to="posts/",blank=True,null=True)
    status = models.CharField(max_length=20,choices=[("draft", "Draft"),("published", "Published"),],default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-created_at"]

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")

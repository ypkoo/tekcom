from django.db import models
# from user.models import User
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Board(models.Model):
    pass

class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(get_user_model(), related_name='articles', on_delete=models.CASCADE)
    title = models.TextField(max_length=255)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__ (self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=255)
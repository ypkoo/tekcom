from django.db import models

# Create your models here.

class Board(models.Model):
    pass

class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    # author = None

    content = models.TextField()
    view_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=255)
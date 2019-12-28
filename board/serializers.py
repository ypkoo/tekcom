from rest_framework import serializers
from .models import Article, Comment

# class ArticleSerializer(serializers):
#     class Meta:
#         model = Article
#         fields = ['content', 'view_count', 'comment_count']

# class CommentSerializer(serializers):
#     class Meta:
#         model = Comment
#         fields = ['content']
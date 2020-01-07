from rest_framework import serializers
from user.models import User
from board.models import Article

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'main_char', 'articles']
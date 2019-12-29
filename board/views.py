from rest_framework import generics

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from .forms import ArticleEditForm
from django.shortcuts import render

def index(request):
    passed = False
    form = ArticleEditForm()

    if request.method == "POST":
        form = ArticleEditForm(request.POST)
        if form.is_valid():
            passed = True
            form = ArticleEditForm()

    return render(request, 'board/article_edit.html', {
        # 'desc1': request.POST.get('desc1'),
        # 'desc2': request.POST.get('desc2'),
        'passed': passed,
        'form': form,
        # 'theme': SUMMERNOTE_THEME,
    })

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
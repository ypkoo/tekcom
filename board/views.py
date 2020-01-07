from rest_framework import generics, permissions

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from .forms import ArticleEditForm
from django.shortcuts import render

from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

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
    # renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# class ArticleList(generics.ListCreateAPIView):
#     # renderer_classes = [JSONRenderer]
#     # queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'board/article_list.html'
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         queryset = Article.objects.all()
#         return Response({'articles': queryset})

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RenderArticleList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    template_name = 'board/article_list.html'

    def get(self, request):
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        queryset = Article.objects.all()
        
        return Response({'articles': queryset, 'username': username, 'test': 'test'})

class RenderArticleDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    template_name = 'board/article_detail.html'

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(pk=self.kwargs['pk'])
        return Response({'article': article})
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
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

# class ArticleList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'article_detail.html'

#     def get(self, request, pk):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request, pk):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
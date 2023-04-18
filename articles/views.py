from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Articles
from .serializers import SerializerArticle
from drf_yasg.utils import swagger_auto_schema

class ArticleAPI(APIView):
    def get(self, request, format=None):
        articles_data = Articles.objects.all()
        articles = SerializerArticle(articles_data, many=True)
        return Response(articles.data)

    @swagger_auto_schema(request_body=SerializerArticle)
    def post(self, request, format=None):
        serializer = SerializerArticle(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):
    def get(self, request, article_id, format=None):
        article = get_object_or_404(Articles,id=article_id)
        serializer = SerializerArticle(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Articles,id=article_id)
        serializer = SerializerArticle(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


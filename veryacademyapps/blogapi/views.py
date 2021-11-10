from rest_framework import generics
from ..blogme.models import Article
from .serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


""" Concrete View Classes


#CreateAPIView
Used for create-only endpoints.


#ListAPIView
Used for read-only endpoints to represent a collection of model instances.


#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.


#DestroyAPIView
Used for delete-only endpoints for a single model instance.


#UpdateAPIView
Used for update-only endpoints for a single model instance.


##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.


RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.


#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.


#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.


"""

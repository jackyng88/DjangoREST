from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from news.models import Article
from news.api.serializers import ArticleSerializer


# The follow article_list and article_detail api_view functions are function
# based views that use the decorator operator (@) to specify functionality.
@api_view(['GET', 'POST'])
def article_list_create_api_view(request):
    # accept requests for all funciton based views
    if request.method == 'GET':
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_api_view(request, pk):
    # retrieve/update/delete data of a specific instance
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({'error': {
                            'code': 404,
                            'message': 'Article not found!'
                            }}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleListCreateAPIView(APIView):
    '''
    Class for creating an Article List inheriting from the APIView class using
    a class-based view as opposed to the function based views we had at the
    beginning.
    '''

    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    # Class based API View for Article Detail

    def get_object(self, pk):
        # Function that calls the DRF get_object_or_404 function
        article = get_object_or_404(Article, pk=pk)
        return article

    def get(self, request, pk):
        # Get function that calls above get_object function
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


    def put(self, request, pk):
        # Put function 
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete function\
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostListSerializer, PostSerializer
from .models import Post


class PostListAPIView(generics.ListAPIView):
    """
    작성된 모든 글 불러오기
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostAPIView(APIView):
    """
    특정 유저가 작성한 글 불러오기
    """
    queryset = Post.objects.none()

    def get(self, request, id):
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

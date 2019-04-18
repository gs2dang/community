from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostListSerializer, PostSerializer
from .models import Post

User = get_user_model()


class PostListAPIView(generics.ListAPIView):
    """
    모든 글 불러오기
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostAPIView(APIView):
    """
    특정 글 불러오기
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, id):
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class UserPostListAPIView(APIView):
    """"
    유저 본인이 작성한 모든 글 불러오기
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(username=request.user)
        post = Post.objects.filter(author__id=user.id)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

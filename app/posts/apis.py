from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostListSerializer, AllPostListSerializer
from .models import Post, PostLike

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
        serializer = AllPostListSerializer(post)
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
        serializer = AllPostListSerializer(post, many=True)
        return Response(serializer.data)


class UserLikeAPIView(APIView):
    """"
    유저 본인이 좋아요 누른 글 불러오기
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(username=request.user)
        post = Post.objects.filter(postlike__author_id=user.id)
        serializer = PostListSerializer(post, many=True)
        return Response(serializer.data)


class SearchAPIView(APIView):
    """
    검색 결과 글 불러오기
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        posts = Post.objects.all()
        search =request.data.get('search', '')

        if search:
            dropdown = request.data.get('dropdown')
            if dropdown == 'title':
                # icontains은 대소문자 구별하지 않음
                posts = posts.filter(title__icontains=search)
            elif dropdown == 'content':
                posts = posts.filter(content__icontains=search)
            elif dropdown == 'nickname':
                posts = posts.filter(author__nickname__icontains=search)
            elif dropdown == 'title-conten':
                posts = posts.filter(title__icontains=search, content__icontains=search)

        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
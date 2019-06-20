from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostListSerializer, AllPostListSerializer, PostModificationSerializer
from .models import Post

User = get_user_model()


class PostListAPIView(APIView):
    """
    모든 글 불러오기
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # generics.ListAPIView
    # queryset = Post.objects.all()
    # serializer_class = PostListSerializer
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =  PostListSerializer(data={**request.data, 'author': request.user.id},)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    """
    특정 글 읽기, 삭제, 수정
    게시글 번호(id)가 있어야 되는 작업이기에 한 곳에 놔뒀다.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializer = AllPostListSerializer(post)
        return Response(serializer.data)

    def delete(self, request, id):
        post = get_object_or_404(Post, id=id, author=request.user)
        post.delete()
        message = {
            "message": "게시글을 삭제했습니다."
        }
        return Response(message, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        post = get_object_or_404(Post, id=id, author=request.user)
        serializer = PostModificationSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
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

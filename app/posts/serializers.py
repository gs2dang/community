from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    """
    좋아요 누른 유저를 제외하고 모든 항목 표시
    """
    class Meta:
        model = Post
        exclude = ('like_user',)


class AllPostListSerializer(serializers.ModelSerializer):
    """
    좋아요 유저 포함하여 모든 항목 표시
    """
    like_user = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostModificationSerializer(serializers.ModelSerializer):
    """
    게시글 수정
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )

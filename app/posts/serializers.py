from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
                  'author',
                  'title',
                  'content',
                  'view_count',
                  'like_count',
                  'created',
                  'modified')


class PostSerializer(serializers.ModelSerializer):
    like_user = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

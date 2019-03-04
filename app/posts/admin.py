from django.contrib import admin

from .models import Post, Comment, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'get_comment_count', 'content_size', 'view_count', 'like_count', 'created', 'modified']
    list_per_page = 20
    search_fields = ['title']

    def content_size(self, obj):
        return len(obj.content)
    content_size.short_description = '글자 수'

    def get_comment_count(self, obj):
        return obj.comment_set.all().count()
    get_comment_count.short_description = '댓글 수'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'get_post_id', 'post', 'created', 'modified']
    list_per_page = 20
    search_fields = ['author__username']

    def get_post_id(self, obj):
        return obj.post.id
    get_post_id.short_description = '게시글 번호'


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'get_author_id', 'post', 'get_post_id', 'created']
    list_per_page = 20

    def get_post_id(self, obj):
        return obj.post.id
    get_post_id.short_description = '포스트 번호'

    def get_author_id(self, obj):
        return obj.author.id
    get_author_id.short_description = '글쓴이 번호'

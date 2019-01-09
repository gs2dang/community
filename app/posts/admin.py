from django.contrib import admin

from .models import Post, Comment, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'get_comment', 'content_size', 'view_count', 'like_count', 'created', 'modified']
    list_per_page = 20
    search_fields = ['title']

    def content_size(self, obj):
        return len(obj.content)
    content_size.short_description = '글자 수'

    def get_comment(self, obj):
        '''
        해당 포스트에 연결된 댓글을 불러옴
        :param obj:
        :return:
        '''
        return obj.comment_set.get(id=4)


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['id', 'author', 'post', 'created', 'modified']
    list_per_page = 20
    search_fields = ['author']


admin.site.register(PostLike)

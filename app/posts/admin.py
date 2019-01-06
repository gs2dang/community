from django.contrib import admin

from .models import Post, Comment, PostLike

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content_size', 'view_count', 'like_count', 'created', 'modified']
    list_per_page = 10
    search_fields = ['title']

    def content_size(self, obj):
        return len(obj.content)
    content_size.short_description = '글자 수'

admin.site.register(Comment)
admin.site.register(PostLike)

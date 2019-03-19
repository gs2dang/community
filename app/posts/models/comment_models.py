from django.conf import settings
from django.db import models

from .post_models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자'
    )
    content = models.TextField('댓글 내용', max_length=200)
    created = models.DateTimeField('작성일', auto_now_add=True)
    modified = models.DateTimeField('수정일', auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = verbose_name

    # 아래 코드는 왜 아닐까?
    # def update_comment_count(self, switch=False):
    #     if switch:
    #         self.post.comment_count += 1
    #         self.save()
    #     else:
    #         self.post.comment_count -= 1
    #         self.save()

from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자'
    )
    title = models.CharField('글 제목', max_length=20)
    content = models.TextField('글 내용', max_length=500)
    photo = models.ImageField('사진', upload_to='post')
    view_count = models.PositiveIntegerField('조회수', default=0)
    like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PostLike'
    )
    created = models.DateTimeField('작성일', auto_now_add=True)
    modified = models.DateTimeField('수정일', auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='작성자'
    )
    content = models.TextField('댓글 내용', max_length=150)
    created = models.DateTimeField('작성일', auto_now_add=True)
    modified = models.DateTimeField('수정일', auto_now=True)

    def __str__(self):
        return self.post


class PostLike(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)

from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='write_posts',
        related_query_name='write_post',
        verbose_name='작성자'
    )
    title = models.CharField('글 제목', max_length=50)
    content = models.TextField('글 내용')
    view_count = models.PositiveIntegerField('조회수', default=0)
    like_count = models.PositiveIntegerField('추천수', default=0)
    like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PostLike'
    )
    created = models.DateTimeField('작성일', auto_now_add=True)
    modified = models.DateTimeField('수정일', auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = '포스트'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    @property
    def update_view_count(self):
        self.view_count += 1
        self.save()

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.id])

    def like_switch(self, author):
        postlike, postlike_created = self.postlike_set.get_or_create(author=author)
        if postlike_created:
            # 추천을 했다(새로 생성)
            self.like_count += 1
        else:
            postlike.delete()
            self.like_count -= 1
        self.save()


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


class PostLike(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='좋아요 누른 사람')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='포스트')
    created = models.DateTimeField('작성일', auto_now_add=True)

    class Meta:
        verbose_name = '추천'
        verbose_name_plural = verbose_name

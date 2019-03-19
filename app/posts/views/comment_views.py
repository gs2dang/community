from django.shortcuts import render, get_object_or_404, redirect

from ..forms import CommentForm
from ..models.post_models import Post
from ..models.comment_models import Comment


def comment_edit(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = Comment.objects.get(pk=comment_pk, post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(post)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'posts/post_edit.html', {'form': form})


def comment_delete(request, post_pk, comment_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        comment = Comment.objects.get(pk=comment_pk, post=post)
        post.update_comment_count()
        # comment.update_comment_count()
        comment.delete()
        return redirect(post)

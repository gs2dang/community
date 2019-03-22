from django.shortcuts import render, get_object_or_404, redirect

from ..forms import CommentForm
from ..models.post_models import Post
from ..models.comment_models import Comment


def comment_new(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            post.update_comment_count(switch=True)
            comment.save()
            return redirect(post)


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
    context = {
        'form': form,
    }
    return render(request, 'comments/comment_edit.html', context)


def comment_delete(request, post_pk, comment_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        comment = get_object_or_404(Comment, pk=comment_pk, post=post)
        post.update_comment_count()
        # comment.update_comment_count()
        comment.delete()
        return redirect(post)

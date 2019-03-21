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


def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    post_id = comment.post.id
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=request.comment)
        if form.is_valid():
            form.save()
            return redirect(post)
    return render(request, 'posts/post_edit.html', {'commentform': CommentForm(instance=request.comment)})


def comment_delete(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk)
        post_id = comment.post.id
        post = get_object_or_404(Post, pk=post_id)
        post.update_comment_count()
        # comment.update_comment_count()
        comment.delete()
        return redirect(post)

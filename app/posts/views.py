from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    search= request.GET.get('search', '')
    if search:
        posts = posts.filter(title__icontains=search)

    context = {
        'posts': posts,
        'search': search,

    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    # 조회수 증가
    post.update_view_count
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


def post_edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
    }
    return render(request, 'posts/post_edit.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)

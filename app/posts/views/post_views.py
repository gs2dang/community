from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from ..forms import PostForm, CommentForm
from ..models.post_models import Post


def post_list(request):
    posts = Post.objects.all()

    # 검색폼에 무언가를 입력하면 search에 그 값이 들어가게 되지만
    # 아무 값도 넣지 않으면 '' 즉 공백이 들어가게 됨
    search = request.GET.get('search', '')
    if search:
        # icontains은 대소문자 구별하지 않음
        posts = posts.filter(title__icontains=search)

    # Show 15 posts per page
    paginator = Paginator(posts, 15)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    # 페이지 범위 설정
    page_numbers_range = 10
    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    if end_index >= max_index:
        end_index = max_index
    paginator_range = paginator.page_range[start_index:end_index]

    context = {
        'posts': posts,
        'search': search,
        'paginator_range': paginator_range,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)

    # 이전에 위치한 주소를 가져오기
    before_url = request.META.get('HTTP_REFERER')

    # 특정 게시글에 바로 접속했을 경우, 해당 게시글이 위치한 페이지 목록으로 갈 수 없기에
    # 게시글 1페이지 이동하게 한다.
    try:
        if '?page=' not in before_url:
            before_url = False
    except TypeError:
        before_url = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            post.update_comment_count(switch=True)
            # comment.update_comment_count(switch=True)
            comment.save()
            return redirect(post)
    else:
        form = CommentForm()

        # 조회수 증가
        post.update_view_count

    context = {
        'post': post,
        'before_url': before_url,
        'form': form,
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
            return redirect(post)
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('posts:post_list')


def post_like(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.like_switch(request.user)
        return redirect(post)

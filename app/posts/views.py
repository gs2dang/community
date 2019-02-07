from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post


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

    # 페이지 범위
    current_page = int(page) if type(page) == str else page
    if current_page < 6:
        start_index = 0
    else:
        start_index = current_page - 6

    if current_page == paginator.num_pages or current_page + 1 == paginator.num_pages:
        end_index = paginator.num_pages
    else:
        end_index = current_page + 5
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

    # 조회수 증가
    post.update_view_count

    context = {
        'post': post,
        'before_url': before_url
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
            return redirect(f'/post/{ post.pk }')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)

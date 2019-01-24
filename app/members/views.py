from django.shortcuts import render, redirect

from .forms import Signup


def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
        return redirect('posts:post_list')
    else:
        form = Signup()

    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)

from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data)
            return redirect('posts:post_list')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data)
            return redirect('posts:post_list')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signin.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post_list')

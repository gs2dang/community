from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model, login, logout
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.shortcuts import render, redirect
from .forms import Signup_Form, LoginForm

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data)
            subject = f'{form.cleaned_data.username}님, 게시판에 오신 것을 환영합니다'
            message = '''
            개인 프로젝트 "게시판"에 가입해 주셔서 감사합니다.
            '''
            to_email = form.cleaned_data.email
            email = EmailMessage(subject, message, to=[to_email])
            email.send()
            return redirect('posts:post_list')
    else:
        form = Signup_Form()

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


@receiver(user_signed_up)
def set_initial_user_names(request, user, sociallogin=None, **kwargs):
    """
    When a social account is created successfully and this signal is received,
    django-allauth passes in the sociallogin param, giving access to metadata on the remote account, e.g.:

    sociallogin.account.provider  # e.g. 'twitter'
    sociallogin.account.get_avatar_url()
    sociallogin.account.get_profile_url()
    sociallogin.account.extra_data['screen_name']

    See the socialaccount_socialaccount table for more in the 'extra_data' field.

    From http://birdhouse.org/blog/2013/12/03/django-allauth-retrieve-firstlast-names-from-fb-twitter-google/comment-page-1/
    """
    # 소셜 로그인을 하면 별명을 받아서 nickname 필드에 넣어준다.
    # receiver 좀 더 알 필요가 있다.
    if sociallogin:
        if sociallogin.account.provider == 'facebook':
            user.nickname = sociallogin.account.extra_data['name']

        if sociallogin.account.provider == 'naver':
            user.nickname = sociallogin.account.extra_data['nickname']
    # 로그인 유형 넣기
    # 예. 네이버로 로그인을 하게 되면 login_type에 naver로 된다.
    user.login_type = sociallogin.account.provider
    user.save()

from django.urls import path

from .apis import PostListAPIView, PostAPIView, UserPostListAPIView

app_name = 'api_post'

urlpatterns = [
    path('list', PostListAPIView.as_view(), name='api_post_list'),
    path('<int:id>', PostAPIView.as_view(), name='api_specific_post'),
    path('list/user', UserPostListAPIView.as_view(), name='api_user_post_list'),
]
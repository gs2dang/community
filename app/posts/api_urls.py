from django.urls import path

from .apis import PostListAPIView, PostAPIView, UserPostListAPIView, UserLikeAPIView, SearchAPIView

app_name = 'api_post'

urlpatterns = [
    path('list', PostListAPIView.as_view(), name='api_post_list'),
    path('<int:id>', PostAPIView.as_view(), name='api_specific_post'),
    path('list/user', UserPostListAPIView.as_view(), name='api_user_post_list'),
    path('list/user/like', UserLikeAPIView.as_view(), name='api_user_like_post_list'),
    path('search', SearchAPIView.as_view(), name='api_search'),
]
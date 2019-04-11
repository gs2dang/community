from django.urls import path

from .apis import UserListAPIView

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='api_user_list'),
]
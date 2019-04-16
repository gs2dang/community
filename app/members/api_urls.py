from django.urls import path

from .apis import UserListAPIView, SpecificUserAPIView

app_name = 'api_user'

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='api_user_list'),
    path('<int:id>/', SpecificUserAPIView.as_view(), name='api_specific_user'),
]
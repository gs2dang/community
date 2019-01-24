from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/create/', views.post_create, name='post_create'),
]
from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('info/', views.info, name='info'),
    path('delete/', views.delete_account, name='delete_account'),
    path('logout_view/', views.logout_view, name='logout_view'),
]
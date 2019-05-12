"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from ckeditor_uploader import views as uploader_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache

urlpatterns_api = [
    path('user/', include('members.api_urls')),
    path('post/', include('posts.api_urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('user/', include('members.urls')),
    path('api/', include(urlpatterns_api)),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/upload/', uploader_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(uploader_views.browse), name='ckeditor_browse'),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

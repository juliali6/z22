"""z22django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from first_app.api.views.router import api_router
from first_app.templates.views import views
from first_app.templates.views.profile import Profile_User
from first_app.templates.views.tags import tags_list, tag_detail
from first_app.templates.views.update_profile import user_redaction
from first_app.templates.views.views import main_page
from views.auth import AuthView
from views.main import PostListView
from views.registration import RegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),
    path('registration', RegistrationView.as_view(), name='reg_page'),
    path('login', AuthView.as_view(), name='login_page'),
    path('create', views.create, name='create'),
    path('posts.py/', PostListView.as_view(), name='posts.py'),
    path('update_profile/', user_redaction, name='update_profile.py'),
    path('profile/', Profile_User.as_view(), name='profile_page'),
    path('api/', include(api_router.urls)),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>', tag_detail, name='tag_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

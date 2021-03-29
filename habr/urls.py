"""habr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", articles, name='articles'),
    path("article/<int:id>/", article_page, name="article"),
    path('authors/', authors, name='authors'),
    path("about/", about, name="about"),
    path("article/<int:pk>/edit/", edit_article, name='article-edit'),
    path("article/add/", add_article, name="article-add"),
    path("article/<int:id>/delete/", delete_article, name="article-delete"),
    path("article/<int:id>/hide/", hide_article, name="article-hide"),
    path("search/", search, name="search"),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

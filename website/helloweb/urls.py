"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("blog/post/<int:id>", views.post, name="post"),
    path("category/<str:name>", views.category, name="category"),
    path("tag/<str:name>", views.tag, name="tag"),
    path("blog/search", views.search, name="search"),
    path("blog/create", views.create, name="create"),
    path("blog/login", LoginView.as_view(), name="blog_login"),
    path("blog/logout/", views.blog_logout, name="blog_logout"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("blog/registration/", views.registration, name="registration"),
    path("blog/profile_update", views.profile_update, name="profile_update"),
]

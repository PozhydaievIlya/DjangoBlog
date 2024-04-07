from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import *
from django.db.models import Q
from django.utils.timezone import now
from .forms import PostForm, UsersForm, CommentForm, ProfilePhotoForm
from .models import Post, Category, Tag, UsersEmail, Comments, Profile
from django.contrib.auth.models import User

def get_categories():
    category = Category.objects.all()
    half = category.count() / 2 + category.count() % 2
    return {'category1': category[:half], 'category2': category[half:]}


def get_tags():
    tag = Tag.objects.all()
    return {'tags': tag}


# Create your views here.


def index(request):
    newPost = Post.objects.get(pk=1)
    posts = Post.objects.order_by("-published_date")
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()
    context = {"posts": posts, "newPost": newPost, "Uform": Uform}
    context.update(get_categories())
    context.update(get_tags())
    # posts = Post.objects.filter(title__contains="NEW")
    # posts = Post.objects.all()
    return render(request, "blog/index.html", context)


def post(request, id=None):
    post = get_object_or_404(Post, pk=id)
    # user email form
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()

    # A comment form
    form = CommentForm(request.POST or None)
    comment = None
    if form.is_valid():
        # Create a Comment object before saving it to the database
        comment = form.save(commit=False)
        comment.post = post
        # Save the comment to the database
        comment.save()
        pass
    # upload profile pictures
    photoForm = ProfilePhotoForm()
    # List of active comments for this article
    comments = post.comments.all().order_by("-date")
    context = {"post": post, "Uform": Uform, "comment": comment, "form": form, "comments": comments, "photoForm": photoForm}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def about(request):
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()
    context = {"Uform": Uform}
    context.update(get_categories())
    return render(request, 'blog/about.html', context)


def contact(request):
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()
    context = {"Uform": Uform}
    context.update(get_categories())
    return render(request, 'blog/contact.html', context)


def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()
    context = {"posts": posts, "Uform": Uform}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def tag(request, name=None):
    t = get_object_or_404(Tag, name=name)
    posts = Post.objects.filter(tags=t).order_by("-published_date")
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()
    context = {"posts": posts, "Uform": Uform}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, 'blog/index.html', context)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query)).order_by("published_date")
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()
    context = {"posts": posts, "Uform": Uform}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, 'blog/index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = now()
            post.save()
            return index(request)
    form = PostForm()
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()
    context = {"form": form, "Uform": Uform}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, 'blog/create.html', context)


def blog_logout(request):
    logout(request)
    return redirect('/')


def blog_login(request):
    if request.method == 'POST':
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()
    context = {"Uform": Uform}
    return render(request, 'registration/login.html', context)


def profile(request):
    currentUser = User.objects.get(id=request.user.id)
    profile_user = Profile.objects.get(user__id=request.user.id)
    if request.method == "POST":
        photoForm = ProfilePhotoForm(request.POST or None, request.FILES or None, instance=profile_user)
        if photoForm.is_valid():
            photoForm.save()
            return redirect('/profile')
        Uform = UsersForm(request.POST)
        if Uform.is_valid():
            Uform.save()
    else:
        Uform = UsersForm()

    photoForm = ProfilePhotoForm()
    context = {"photoForm": photoForm, "Uform": Uform}
    return render(request, 'blog/profile.html', context)
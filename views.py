from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PostForm, CommentForm
from .models import Post, Comment, Like, Follow, User

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "blog/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def home_view(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("post_detail", pk=pk)
    else:
        form = CommentForm()
    return render(request, "blog/post_detail.html", {"post": post, "form": form})

@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})

@login_required
def like_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Like.objects.get_or_create(post=post, user=request.user)
    return redirect("post_detail", pk=pk)

@login_required
def follow_author_view(request, user_id):
    author = get_object_or_404(User, pk=user_id)
    Follow.objects.get_or_create(follower=request.user, following=author)
    return redirect("profile", user_id=user_id)

def profile_view(request, user_id):
    user_profile = get_object_or_404(User, pk=user_id)
    return render(request, "blog/profile.html", {"user_profile": user_profile})

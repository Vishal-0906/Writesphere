from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Comment

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','role']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','cover_image','categories','tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

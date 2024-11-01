from django import forms
from .models import Category, Post, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = 'name',


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'category'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'author', 'text'

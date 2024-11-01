from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from .forms import CategoryForm, PostForm, CommentForm


def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()

    ctx = {
        'posts': posts, 'form': form
    }

    return render(request, 'test_app/index.html', ctx)


def categories(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()

    ctx = {
        'categories': categories,
        'form': form
    }

    return render(request, 'test_app/categories.html', ctx)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.posts.all()

    ctx = {
        'category': category, 'posts': posts
    }
    return render(request, 'test_app/category_detail.html', ctx)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    ctx = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'test_app/post_detail.html', ctx)

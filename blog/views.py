# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-created_at')
    return render(request, 'blog/category_list.html', {'category': category, 'posts': posts})


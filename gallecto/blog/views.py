from django.shortcuts import render
from .models import *
from .forms import CommentForm


def blog_page(request):
    context = {
        "title": "文章分类 - Gallecto 博客",
        "name": "按分类浏览博客文章",
        "categories": Category.objects.filter(status=1),
    }
    return render(request, "blog.html", context)


def post_list(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category_id=category.id, status=1)

    context = {
        "title": category.title,
        "category": category,
        "posts": posts,
        "categories": Category.objects.filter(status=1),
    }
    return render(request, 'post_list.html', context)


def post_view(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post.id, parent__isnull=True)

    post_comments = []
    for comment in comments:
        comment_dict = comment.__dict__
        replies = Comment.objects.filter(parent=comment.id)
        if replies.exists():
            comment_dict["replies"] = [reply.__dict__ for reply in replies]
        post_comments.append(comment_dict)

    context = {
        "title": post.title,
        "post": post,
        "categories": Category.objects.filter(status=1),
    }
    if comments.exists():
        context["comments"] = post_comments

    return render(request, "post.html", context)


def show_comment(request):
    form = CommentForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request, "modals/comment_creation.html", context)


def create_comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        return render(request, 'modals/comment_creation_success.html', {})

    context = {
        "form": form
    }
    return render(request, "modals/comment_creation.html", context)

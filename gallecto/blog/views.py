from django.shortcuts import render
from .models import *

# Create your views here.
def blog_page(request):
	context = {}
	context["title"] = "BLOG PAGE"
	context["name"] = "BLOG PAGE INFO"

	data = Category.objects.filter()
	context["categories"] = data
	return render(request, "blog.html", context)

def post_list(request, slug):
	context = {}
	category = Category.objects.get(slug=slug)
	context["title"] = category.title

	posts = Post.objects.filter(category_id=category.id)
	context["posts"] = posts

	return render(request, 'post_list.html', context)

def post_view(request, slug):
	context = {}
	post = Post.objects.get(slug=slug)
	context["post"] = post

	comments = Comment.objects.filter(post = post.id, parent__isnull = True)
	post_comments = []
	for comment in comments:
		comment_dict = comment.__dict__
		replies = Comment.objects.filter(parent= comment.id)

		if replies.exists():
			comment_dict["replies"] = []
			for reply in replies:
				comment_dict["replies"].append(reply.__dict__)
		
		post_comments.append(comment_dict)

	if comments.exists():
		context["comments"] = post_comments
	
	return render(request, "post.html", context)
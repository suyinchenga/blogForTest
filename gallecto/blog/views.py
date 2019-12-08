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

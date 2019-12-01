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
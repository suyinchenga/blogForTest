from django.shortcuts import render

# Create your views here.
def blog_page(request):
	context = {}
	context["title"] = "BLOG PAGE"
	context["name"] = "BLOG PAGE INFO"
	return render(request, "blog.html", context)
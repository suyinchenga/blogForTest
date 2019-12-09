from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	context = {}
	context["title"] = "HOME PAGE"
	context["name"] = "HOME PAGE INFO"
	return render(request, "home.html", context)

def gallecto_404(request, exception):
	context = {}
	return render(request, "404.html", context)
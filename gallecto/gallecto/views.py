from django.shortcuts import render


def home_page(request):
    context = {
        "title": "写技术，也写成长 - Gallecto 技术博客",
    }
    return render(request, "home.html", context)


def gallecto_404(request, exception):
    return render(request, "404.html", {})

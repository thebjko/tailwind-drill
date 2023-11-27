from django.shortcuts import render


def index(request):
    return render(request, 'layouts/index.html')

def grid(request):
    return render(request, 'layouts/css-grid.html')

def flexbox(request):
    return render(request, 'layouts/flexbox.html')

def blog(request):
    return render(request, 'layouts/blog.html')

def challenges(request):
    return render(request, 'layouts/challenges.html')
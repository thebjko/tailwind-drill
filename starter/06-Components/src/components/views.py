from django.shortcuts import render

# Create your views here.
def accordion(request):
    return render(request, 'components/accordion.html')


def carousel(request):
    return render(request, 'components/carousel.html')


def table(request):
    return render(request, 'components/table.html')


def paginator(request):
    return render(request, 'components/paginator.html')
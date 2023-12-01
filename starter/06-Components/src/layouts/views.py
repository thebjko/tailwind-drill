from django.shortcuts import render

# Create your views here.
def hero(request):
    return render(request, 'layouts/hero.html')


def email(request):
    return render(request, 'layouts/email.html')
from django.shortcuts import render
from django.views import generic


class IndexTemplateView(generic.TemplateView):
    template_name = 'omnifoods/index.html'
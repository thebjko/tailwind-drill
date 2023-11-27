from django.urls import path

from . import views

app_name = 'layouts'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('grid/', views.grid, name='grid'),
    path('flexbox/', views.flexbox, name='flexbox'),
    path('blog/', views.blog, name='blog'),
    path('challenges/', views.challenges, name='challenges'),
]
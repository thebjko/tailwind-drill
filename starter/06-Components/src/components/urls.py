from django.urls import path

from . import views

app_name = 'components'
urlpatterns = [
    path('accordion/', views.accordion, name='accordion'),
    path('carousel/', views.carousel, name='carousel'),
]
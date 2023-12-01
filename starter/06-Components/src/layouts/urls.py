from django.urls import path

from . import views


app_name = 'layouts'
urlpatterns = [
    path('hero/', views.hero, name='hero'),
    path('email/', views.email, name='email'),
]
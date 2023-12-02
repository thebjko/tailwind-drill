from django.urls import path

from . import views

app_name = 'omnifoods'
urlpatterns = [
    path("", views.IndexTemplateView.as_view(), name="index"),
]
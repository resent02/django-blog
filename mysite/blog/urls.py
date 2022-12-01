from . import views
from django.urls import path

urlpatterns = [
    path("blog/", views.index),
    path("", views.main_page),
    path("blog/<pub>", views.pub_view)
]

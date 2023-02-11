from django.urls import path
from . import views

app_name = 'blog'

urlpattern = [
    path("", views.blog, name='blog'),
    path("<int:blog_id>/", views.detail, name='detail'),
]
from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    blog = Blog.objects.order_by('-date')    # сортирование по дате по убыванию
    return render(request, 'blog/blogs.html', {'blogs': blog})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return request(request, 'blog/details.html', {'blog': blog})







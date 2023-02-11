from django.shortcuts import render
from .models import Blog


def blogs(request):
    blog = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'id': blog})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return request(request, 'blog/detail.html', {'blog': blog})







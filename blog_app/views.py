from django.shortcuts import render, get_object_or_404
from blog_app.models import Blog  # new


# Create your views here.
def index(request):
    blogs = Blog.objects.all().order_by('-created')  # new

    context = {
        "blogs": blogs
    }
    return render(request, 'blog/index.html', context=context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    context = {
        "blog": blog
    }
    return render(request, 'blog/detail.html', context=context)

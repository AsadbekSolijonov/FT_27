from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from blog_app.models import Blog  # new


# Create your views here.
def index(request):
    blogs = Blog.objects.all().order_by('-created')  # new

    paginator = Paginator(blogs, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "blogs": page_obj
    }
    return render(request, 'blog/index.html', context=context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    next_article = Blog.objects.filter(pk__gt=pk).order_by('pk').first()
    previous_article = Blog.objects.filter(pk__lt=pk).order_by('-pk').first()

    context = {
        "blog": blog,
        'next_article': next_article,
        'previous_article': previous_article
    }
    return render(request, 'blog/detail.html', context=context)


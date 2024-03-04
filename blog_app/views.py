from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from blog_app.forms import CommentForm
from blog_app.models import Blog, Comment  # new


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
    comments = Comment.objects.filter(blog_id=pk).order_by('-created')  # new

    # Forms connection and save to database
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', pk)  # new
    else:
        form = CommentForm()

    context = {
        "blog": blog,
        'next_article': next_article,
        'previous_article': previous_article,
        'form': form,
        'comments': comments

    }
    return render(request, 'blog/detail.html', context=context)

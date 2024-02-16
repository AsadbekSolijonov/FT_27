from django.shortcuts import render, HttpResponse
from blog_app.models import Blog  # new
import random
import datetime


# Create your views here.
def index(request):
    blogs = Blog.objects.all().order_by('-created')  # new

    context = {
        "blogs": blogs
    }
    return render(request, 'blog/index.html', context=context)

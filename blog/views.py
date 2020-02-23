from django.shortcuts import render, get_object_or_404

from django.views import generic
from django.http import Http404

from . import models

from django.contrib import messages
# Create your views here.

class BlogList(generic.ListView):
    paginate_by = 5
    model=models.Blog

def detail(request, blog_id):
    detailblog = get_object_or_404(models.Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog':detailblog})

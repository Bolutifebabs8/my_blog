from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from blog.models import BlogPost
from .forms import CommentForm

def comment_create(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = obj
            comment.save()
            form = CommentForm()
            return redirect(f'/blog/{slug}')  # Redirect back to the blog post detail page
    else:
       form = CommentForm()
    return redirect(f'/blog/{slug}')





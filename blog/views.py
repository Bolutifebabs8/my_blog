from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm
from comments.forms import CommentForm

# GET -> Retrieve/List

# POST -> Create / Update / Delete

def blog_post_list_view(request):
    # list out objects
    # search list
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(author=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


@login_required
def blog_post_create_view(request):
    # create objects
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'create.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'detail.html'
    comment_form = CommentForm()
    context ={'object': obj, 'form': comment_form}
    return render(request, template_name, context)


@login_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None,  request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(f"/blog/{obj.slug}")
    template_name = 'update.html'
    context ={'title': f"Edit - {obj.title}", 'form': form}
    return render(request, template_name, context)


@login_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context ={'object': obj}
    return render(request, template_name, context)
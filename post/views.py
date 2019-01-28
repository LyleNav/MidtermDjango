from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm, CommentModelForm
from datetime import datetime

# Create your views here.
def index(request):
    context = {}
    p = Post.objects.all()
    context['posts'] = p
    return render(request, 'index.html', context)

def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id = post_id)
    return render(request, 'detail.html', context)

def create(request):
    context = {}
    context['form'] = PostModelForm()
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/post/')
        else:
            context['form'] = form
            return render(request, 'create.html', context)
    else:
        return render(request, 'create.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/post/')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
    return render(request, 'update.html', context)

def comment(request, post_id):
    context = {}
    context['form'] = CommentModelForm(initial={'post':Post.objects.get(id=post_id)})
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/post/')
        else:
            context['form'] = form
            return render(request, 'comment.html', context)
    else:
        return render(request, 'comment.html', context)
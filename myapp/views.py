from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm,PostUpdateForm,CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'index.html',context)
@login_required
def about(request):
    return HttpResponse('<h1 style="color: blue">About page</h1>')
@login_required
def write(request):
    posts=Post.objects.all()
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('index')   
    else:
        form=PostForm()
    context={
        'form':form
    }
    return render(request,'write.html',context)

    
@login_required
def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        c_form=CommentForm(request.POST)
        if c_form.is_valid():
            instance=c_form.save(commit=False)
            instance.user=request.user
            instance.post=post
            instance.save()
            return redirect('post_detail',pk=post.id)
    else:
        c_form=CommentForm()    
        
    context={
        'post':post,
        'c_form':c_form
    }
    
    return render(request,'post_detail.html',context)
@login_required
def post_edit(request,pk):
    post=Post.objects.get(id=pk)
    if(request.method=='POST'):
        form=PostUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=post.id)
    else:
        form=PostUpdateForm(instance=post)    
    context={
        'post':post,
        'form':form
    }
    return render(request,'post_edit.html',context)

@login_required
def post_delete(request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('index')
        
        
    context={
        'post':post
    }
    return render(request,'post_delete.html',context)


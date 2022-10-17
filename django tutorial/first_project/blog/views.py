from logging import WARNING
from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post,PostGerne,Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import PostCreationForm,PostCreationForm2
from django.contrib import messages


def home(request):
    post_list=Post.objects.all().order_by('-edit_date')
    paginator=Paginator(post_list,5)
    page=request.GET.get('page')
    if page:
        object=paginator.page(page)
    else:
        object=paginator.page(1)
    context={'object':object,
            'objects':paginator}
    return render(request,'blog/home.html',context)

@login_required(login_url='login')
def create_post(request):
    form1=PostCreationForm()
    form2=PostCreationForm2()
    context={'form1':form1,'form2':form2}
    if request.method=='POST':
        print(request.POST)
        form1=PostCreationForm(request.POST)
        form1.instance.owner=request.user
        if form1.is_valid():
            post=form1.save()
            post.gerne.set(request.POST.getlist('gerne'))
            return redirect('blog-home')
    return render(request,'blog/create-post.html',context)

@login_required(login_url='login')
def edit_post(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
    except:
        messages.warning(request,'You are going wrong way!!')
        return redirect('blog-home')
    if post.owner != request.user:
        messages.warning(request,'You cannot edit other\'s post!!')
        return redirect('blog-home')
    form1=PostCreationForm(instance=post)
    form2=PostCreationForm2(instance=post)
    context={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=PostCreationForm(request.POST,instance=post)
        if form1.is_valid():
            post=form1.save()
            post.gerne.set(request.POST.getlist('gerne'))
            return redirect('blog-home')
    return render(request,'blog/edit-post.html',context)

def view_post(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
    except:
        messages.warning(request,'You are going wrong way!!')
        return redirect('blog-home')
    context={'post':post}
    return render(request,'blog/view-post.html',context)

@login_required(login_url='login')
def delete_post(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
    except:
        messages.warning(request,'You are going wrong way!!')
        return redirect('blog-home')
    context={'post':post}
    if request.method=="POST":
        post.delete()
        messages.success(request,f'Deleted {post.title} successful!')
        return redirect('blog-home')
    return render(request,'blog/delete-post.html',context)

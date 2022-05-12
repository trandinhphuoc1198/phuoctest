from base64 import decode
from django.shortcuts import render,redirect
from .models import Room,Topic,Message
from .forms import Roomform,Messageform
from django.db.models import Q
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
import time
def home(request):
    return render(request,'main/home.html')
def room(request,pk=None):
    
    q=request.GET.get('w')
    if q:
        rooms=Room.objects.filter(Q(topic__title=q) | 
        Q(name__icontains=q))
    else:
        rooms=Room.objects.all()
    topic=Topic.objects.all()
    context={'rooms':rooms,
            'topic':topic}
    if pk==None:
        return render(request,'main/room.html',context)
    else:
        rooms=Room.objects.get(id=pk)
        messages=rooms.message_set.all().order_by('-created')
        context={'rooms':rooms,'messages':messages}
        if request.method=="POST":
            message=Message.objects.create( 
                user=request.user,
                room=rooms,
                content=request.POST.get('content')
                )
        return render(request,'main/specific_room.html',context)
@login_required(login_url='log_in')
def create_room(request):
    form=Roomform()
    context={'form':form}
    print(request.method)
    if request.method=='POST':
        form=Roomform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room')
    return render(request,'main/room_form.html',context)
def update_room(request,pk):
    room=Room.objects.get(id=pk)
    form=Roomform(instance=room)
    context={'form':form}
    if request.method=='POST':
        form=Roomform(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('room')
    return render(request,'main/room_form.html',context)
def delete_room(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('room')
    return render(request,'main/delete_form.html',{'room':room})
def log_in(request):
    command='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('room')
        else:
            messages.error(request,'user name or passwork sucks')
    return render(request,'main/login.html',{'command':command})
def log_out(request):
    logout(request)
    try:
        a=request.META['HTTP_REFERER']
    except:
        return HttpResponse('No')
    return redirect(a)
def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('room')
        else:
            messages.error(request,'wrong!!')
            
    return render(request,'main/login.html',{'form':form})
def delete_message(request,pk):
    if message:=Message.objects.get(id=pk):
        message.delete()
    else:
        messages.error(request,'message not exist!!')
    return redirect(request.META['HTTP_REFERER'])

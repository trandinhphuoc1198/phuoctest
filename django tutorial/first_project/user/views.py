from django.shortcuts import render,redirect
from django.contrib import messages
from blog.forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm,UpdateProfileImageForm

# Create your views here.
HOME='blog-home'
ENDPOINT='http://localhost:8000'

def register(request):
    form=UserRegisterForm()
    next=request.GET.get('next')
    context={'form':form,
            'next':next}
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.add_message(request,messages.SUCCESS,f'Account has been created successfully for {form.cleaned_data["username"]}')
            login(request,user=user)
            if next:
                return redirect(ENDPOINT+next)
            return redirect(HOME)
        else:
            msgs=form.errors.values()
            for msg in list(msgs):
                messages.add_message(request,messages.WARNING,f'{msg}')
    return render(request,'user/register.html',context)

def login_view(request):
    next=request.GET.get('next')
    context={'next':next}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user=user)
            messages.add_message(request,messages.SUCCESS,f'Welcome back, {username}!!')
            if next:
                return redirect(ENDPOINT+next)
            return redirect(HOME)
        else:
            messages.add_message(request,messages.WARNING,f'ID or Password is wrong!')
    return render(request,'user/login.html',context)

@login_required(login_url='login')
def update_profile(request):
    u_form=UserUpdateForm(instance=request.user)
    p_form=UpdateProfileForm(instance=request.user.profile)
    i_form=UpdateProfileImageForm(instance=request.user)
    context={'u_form':u_form,
            'p_form':p_form,
            'i_form':i_form}
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=UpdateProfileForm(request.POST,instance=request.user.profile)
        i_form=UpdateProfileImageForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() and i_form.is_valid():
            u_form.save()
            p_form.save()
            i_form.save()
            messages.add_message(request,messages.SUCCESS,f'Update profile successfully!')
            return redirect('update_profile')
    return render(request,'user/update_profile.html',context)
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,f'Logged out!')
    return redirect(HOME)

@login_required(login_url='login')
def profile(request):
    return render(request,'user/profile.html')

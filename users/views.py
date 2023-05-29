from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from .forms import *
from .urls import *
def signup(request):
    if request.method =='POST':
          form=SignupForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect("http://localhost:8000")
    else:
        form=SignupForm()          

    context={
        'form':form
    }
    return render(request,'users/signup.html',context)
@login_required
def profile(request):
    if(request.method=='POST'): 
        u_form=UserUpdateForm(request.POST or None, instance=request.user)
        p_form=ProfileUpdateForm(request.POST or None,request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('http://127.0.0.1:8000/user/profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profilemodel)
    context={
        'u_form':u_form,
        'p_form':p_form,
    } 
    return render(request,'users/profile.html',context)
    

    

# Create your views here.

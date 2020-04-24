from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import forms
# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponse("logout sucess")

def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'account/home.html',context={'user':user})
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("user not fond")
    else:
        return render(request,'account/index.html',context={})

def register(request):

    user_form = forms.user_form()
    profile_form = forms.profile_form()

    if request.method == "POST":
        user = forms.user_form(request.POST)
        profile = forms.profile_form(request.POST)

        if user.is_valid() and profile.is_valid():

            user_data = user.save()
            user_data.set_password(user_data.password)
            user_data.save()

            profile_data = profile.save(commit=False)
            profile_data.user = user_data
            profile_form.email = user_data.email

            if "profile_pic" in request.FILES:
                profile_data.profile_pic = request.FILES['profile_pic']
                profile_data.save()
                return render(request,'account/index.html',context={})
            else:
                return render(request,'account/signup.html',context={'user':user_form,'profile':profile_form,'msg':"FILE IS NOT VALID"})
        else:
            return render(request,'account/signup.html',context={'user':user_form,'profile':profile_form,'msg':'FORM IS NOT VALID'})
    else:
        return render(request,'account/signup.html',context={'user':user_form,'profile':profile_form})
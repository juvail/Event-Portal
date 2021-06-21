from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import Accounts,Login
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

def accounts(request , *args , **kwargs):
    form = Accounts(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"already have an account")
            else:
                User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                User.save
                return redirect("/account/login")
    return render(request , 'auth.html' , {"form":form,"already":"already have account"})



def login_view(request , *args,**kwargs):
    form = Login(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        if user!=None:
            login(request,user)
            return redirect("/user-profile")
        else:
            messages.info(request,"Invalid user please register first")
            return redirect("/account")
    forget_password = "forget password?"
    return render(request,'auth.html',{"form":form,"forget":forget_password})


def logout_view(request):
    logout(request)
    return redirect("/")
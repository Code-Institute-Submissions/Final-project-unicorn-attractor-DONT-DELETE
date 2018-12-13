from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm

# <---------- REGISTER FORM  ---------->

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created {username}, you can now login! ")
            return redirect("index")
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {'form': form })

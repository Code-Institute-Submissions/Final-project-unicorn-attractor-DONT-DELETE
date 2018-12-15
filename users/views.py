from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# <---------- REGISTER FORM  ---------->

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Your account has been created, you can now login! ")
            return redirect(reverse("login"))
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {'form': form })


@login_required
def profile(request):

    return render(request, "profile.html")
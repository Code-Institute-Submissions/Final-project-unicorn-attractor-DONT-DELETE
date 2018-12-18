from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UpdateUserForm, UpdateUserProfile

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

    if request.method == "POST":
        User_Profile = UpdateUserProfile(request.POST, instance=request.user)
        User_Form = UpdateUserForm(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)

        if User_Profile.is_valid() and User_Form.is_valid():
            User_Form.save()
            User_Profile.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")
    else:
        User_Profile = UpdateUserProfile(instance=request.user.profile)
        User_Form = UpdateUserForm(instance=request.user)

    context = {
        "Profile_Form": User_Profile,
        "User_Form": User_Form
    }

    return render(request, "profile.html", context)

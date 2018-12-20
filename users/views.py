from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UpdateImage, UpdateProfile
from bug.models import Bug
from feature.models import Feature

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
        User_profile = UpdateProfile(request.POST, instance=request.user)
        User_image = UpdateImage(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)

        if User_profile.is_valid() and User_image.is_valid():
            User_image.save()
            User_profile.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")
    else:

        User_profile = UpdateProfile(instance=request.user)
        User_image = UpdateImage(instance=request.user.profile)

        print(User_image)    
        print(User_profile) 

        ProfileBug = Bug.objects.filter(author=request.user)
        ProfileFeature = Feature.objects.filter(author=request.user)

    context = {
        "User_profile": User_profile,
        "User_image": User_image,
        "ProfileBug": ProfileBug,
        "ProfileFeature": ProfileFeature,
    }

    return render(request, "profile.html", context)

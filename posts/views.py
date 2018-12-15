from django.shortcuts import render, reverse, redirect
from django.contrib import auth, messages
from posts.models import Create_post
from .forms import New_posts

# Create your views here.

def index(request):
   

    return render(request, "index.html")

def create_post(request):
    if request.method == "POST":
        form = New_posts(request.POST)

        if form.is_valid():
            messages.success(request, "Your post has been posted!")
            form.save()
            return redirect(reverse("index"))
    else:
        form = New_posts()
    

    return render(request, "new_posts.html", {'form':form})

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Feature
from .forms import New_posts


@login_required
def create_feature(request):
    if request.method == "POST":
        form = New_posts(request.POST)

        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            messages.success(request, "Your post has been created!")
            form.save()
            return redirect(reverse("index"))
    else:
        form = New_posts()

    return render(request, "new_feature.html", {'form': form})

def preview_feature(request, id):
    
    feature = get_object_or_404(Feature, pk=id)
    feature.views += 1

    context = {
        "post": feature,
    }
    return render(request, "preview_feature.html", context)
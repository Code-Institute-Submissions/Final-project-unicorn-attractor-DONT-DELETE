from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Feature
from .forms import New_posts, Comment_form


@login_required
def create_feature(request):
    if request.method == "POST":
        form = New_posts(request.POST)

        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            messages.success(request, "Your post has been created!")
            form.save()
            return redirect(reverse("profile"))
    else:
        form = New_posts()

    return render(request, "new_feature.html", {'form': form})

def preview_feature(request, id):
    
    feature = get_object_or_404(Feature, pk=id)
    comment = Comment_form
    feature.views += 1

    context = {
        "post": feature,
        "comment": comment,
    }
    return render(request, "preview_feature.html", context)

@login_required
def delete_feature(request, id):

    feature = get_object_or_404(Feature, pk=id)

    if request.method == "POST":
        feature.delete() 
        
        return redirect(reverse("profile"))
    else:

        context = {
        "feature": feature,
        }


    return render(request, "delete_feature.html", context)

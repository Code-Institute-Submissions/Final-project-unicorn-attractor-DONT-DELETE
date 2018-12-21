from django.shortcuts import render
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import New_posts, Comment_form
from .models import Bug

# Create your views here.
@login_required
def create_bug(request):
    if request.method == "POST":
        form = New_posts(request.POST)

        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            messages.success(request, "Your post has been created!")
            return redirect(reverse("profile"))
    else:
        form = New_posts()

    return render(request, "new_bug.html", {'form': form})


def preview_bug(request, id):

    bug = get_object_or_404(Bug, pk=id)
    bug.views += 1

    if request.method == "POST":
        comment = Comment_form(request.POST)
        
        if comment.is_valid():
            comments = comment.save(commit=False)
            comments.bug = bug
            comments.author = request.user
            comments.save()

            return redirect(reverse("home"))

    else:
        comment = Comment_form()

        context = {
            "bug": bug,
            "comment": comment,
            }
    return render(request, "preview_bug.html", context)

@login_required
def delete_bug(request, id):
    bug = get_object_or_404(Bug, pk=id)
    
    if request.method == "POST":
        bug.delete() 
        return redirect(reverse("profile"))
    else:
        context = {
        "bug": bug,
        }
    return render(request, "delete_bug.html", context)




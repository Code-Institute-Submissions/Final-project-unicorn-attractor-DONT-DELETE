from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import New_posts, Comment_form, BugComment
from .models import Bug


def preview_bug(request, id):
    bug = get_object_or_404(Bug, pk=id)

    if request.user != bug.author and bug.assigned:
        bug.views += 1
        bug.save()

    all_comments = BugComment.objects.filter(bug=bug)
    if request.method == "POST":
        comment = Comment_form(request.POST)

        if comment.is_valid():
            comments = comment.save(commit=False)
            comments.bug = bug
            comments.author = request.user
            comments.save()
            return redirect(preview_bug, bug.id)

    else:
        comment = Comment_form()
        context = {
            "bug": bug,
            "comment": comment,
            "comments": all_comments,
        }
    return render(request, "preview_bug.html", context)


def upvote_bug(id):
    bug = get_object_or_404(Bug, pk=id)
    bug.upvotes += 1
    bug.save()

    return redirect("home")


@login_required
def create_bug(request):
    form = New_posts()
    if request.method == "POST":
        form = New_posts(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            messages.success(request, "Your post has been created!")
            return redirect(reverse("profile"))

    context = {
        "form": form,
    }
    return render(request, "create_bug.html", context)


@login_required
def edit_bug(request, id):
    edit_bug = get_object_or_404(Bug, pk=id)

    if request.method == "POST":
        form = New_posts(request.POST, instance=edit_bug)

        if form.is_valid() and edit_bug.author == request.user:
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            messages.success(request, "Your post has been successful!")
            return redirect('profile')

        elif form.is_valid():
            bug = form.save(commit=False)
            bug.save()
            messages.success(request, "Your post has been successful!")
            return redirect('profile')

    context = {
        "edit_bug": edit_bug,
    }

    return render(request, "edit_bug.html", context)


@login_required
def add_bug(request, id):
    add_bug = get_object_or_404(Bug, pk=id)

    if request.method == "POST":
        form = New_posts(request.POST, instance=add_bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.assigned = str(request.user)
            bug.status = "Doing"
            bug.save()
            messages.success(request, "Congratulations bug added!")
            return redirect("profile")

    context = {
        "bugDetail": add_bug,
    }

    return render(request, "add_bug.html", context)


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

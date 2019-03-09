from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Feature
from .forms import New_posts, Comment_form, FeatureComment
from django.contrib import messages


def preview_feature(request, id):
    feature = get_object_or_404(Feature, pk=id)

    if request.user != feature.author:
        feature.views += 1
        feature.save()

    all_comments = FeatureComment.objects.filter(
        feature=feature)

    if request.method == "POST":
        comment = Comment_form(request.POST)

        if comment.is_valid():
            comments = comment.save(commit=False)
            comments.feature = feature
            comments.author = request.user
            comments.save()
            return redirect(preview_feature, feature.id)

    else:
        comment = Comment_form()
        context = {
            "feature": feature,
            "comment": comment,
            "comments": all_comments,
        }
    return render(request, "preview_feature.html", context)


def upvote_feature(request, id):
    feature = get_object_or_404(Feature, pk=id)
    feature.upvotes += 1
    feature.save()
    messages.success(request,
                     "Feature has been Upvoted, Thank you")
    return redirect("home")


@login_required
def create_feature(request):
    form = New_posts()

    if request.method == "POST":
        form = New_posts(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            messages.success(request,
                             "Your Feature has been created!")
            return redirect(reverse("profile"))
    else:
        context = {
            "form": form,
        }
    return render(request, "create_feature.html", context)


@login_required
def edit_feature(request, id):
    feature = get_object_or_404(Feature, pk=id)

    if request.method == "POST":
        form = New_posts(request.POST, instance=feature)

        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            messages.success(request,
                             "Feature has been edited successfully!")
            return redirect(preview_feature, feature.id)
    else:
        form = New_posts(instance=feature)

        context = {
            "form": form,
        }
    return render(request, "edit_feature.html", context)


@login_required
def delete_feature(request, id):
    feature = get_object_or_404(Feature, pk=id)

    if request.method == "POST":
        feature.delete()
        messages.info(request,
                      "Your Feature has been deleted!")
        return redirect(reverse("profile"))
    else:
        context = {
            "feature": feature,
        }
    return render(request, "delete_feature.html", context)

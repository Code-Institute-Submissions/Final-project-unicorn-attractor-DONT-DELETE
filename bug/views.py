from django.shortcuts import render
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import auth, messages
from .forms import New_posts, Bug
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_bug(request):
    if request.method == "POST":
        form = New_posts(request.POST)

        if form.is_valid():
            author_id = request.user
            messages.success(request, "Your post has been created!")
            form.save()
            return redirect(reverse("index"))
    else:
        form = New_posts()

    return render(request, "new_posts.html", {'form': form})


def preview_bug(request, id):
    post = get_object_or_404(Posts, pk=id)
    comment = Bug()

    post.views += 1

    context = {
        "post": post,
        "comment": comment
    }
    return render(request, "preview_bug.html", context)

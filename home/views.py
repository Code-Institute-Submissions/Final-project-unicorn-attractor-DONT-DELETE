from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from bug.models import Bug
from feature.models import Feature

# <-------------- LANDING PAGE ----------->
def index(request):    

    return render(request, "index.html")


# <--------------- HOMEPAGE ONCE LOGGED IN --------->
@login_required
def home(request):

    features = Feature.objects.all()
    bugs = Bug.objects.all()

    context = {
        "bugs": bugs,
        "features": features,
    }
    return render(request, "home.html", context)





from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bug.models import Bug
from feature.models import Feature

# <-------------- LANDING PAGE ----------->
def index(request):    

    return render(request, "index.html")


# <--------------- HOMEPAGE ONCE LOGGED IN --------->
@login_required
def home(request):
    
    bugs = Bug.objects.all()
    features = Feature.objects.all()

    context = {
        "bugs": bugs,
        "features": features,
    }
    return render(request, "home.html", context)





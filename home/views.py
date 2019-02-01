from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from bug.models import Bug
from feature.models import Feature
from django.contrib.auth.models import User
from django.http import JsonResponse

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


def statistics(request):

    return render(request, "stats.html")

def data_for_graphs(request):
    """
    collect all data for graphs to display and return data as a json response for chart.js to process
    """
    # Total amount on of data on website.
    total_features = Feature.objects.all().count()
    total_bugs = Bug.objects.all().count()
    total_users = User.objects.all().count()

    # Bugs Status
    todo = Bug.objects.filter(status='Todo').count()
    doing = Bug.objects.filter(status='Doing').count()
    done = Bug.objects.filter(status='Done').count()

    bugStats = [todo, doing, done]
    totalResults = [total_features, total_bugs, total_users]
    
    data = {
        'totals': totalResults,
        'bugStats': bugStats,
    }

    return JsonResponse(data, safe=False)


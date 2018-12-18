from django.shortcuts import render
from bug.models import Bug
from feature.models import Feature


def index(request):    

    return render(request, "index.html")

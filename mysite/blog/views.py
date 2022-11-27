from django.shortcuts import render
from .models import Publication
from django.utils import timezone


# Create your views here.

def index(request):
    publications = Publication.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/index.html", {'publications': publications})

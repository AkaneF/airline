from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Flight

# Create your views here.
def index(request):
    return HttpResponse('Flights')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mahi(request):
    return HttpResponse('<marquee><h1>I love brother and sister Relationship</h1>')


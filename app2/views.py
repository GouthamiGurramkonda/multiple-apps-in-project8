from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def family(request):
    return HttpResponse('<h1>I love my family</h1>')

def girl(request):
    return HttpResponse('<h1>Girls are buetiful</h1>')


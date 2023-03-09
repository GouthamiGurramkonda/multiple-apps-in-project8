from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mom(request):
    return HttpResponse('<h1>mom is the best person in the world</h1>')

def dad(request):
    return HttpResponse('<h1>my dad is my best frinend</h1>')


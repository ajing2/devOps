from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("hello salt")

def installApp(request):
    return render(request, 'installapp.html')
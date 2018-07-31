from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello ansible")

def test(request):
    return HttpResponse("<h1>test 就是这么拽</h1>")
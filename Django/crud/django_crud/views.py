from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hellow_world(request):
    return HttpResponse('hii world')
def render_page(request):
    return  render (request,'view/index.html')
def brian(request,name):
    return HttpResponse(f"hello world ,{name.capitalize()} !!!!!")
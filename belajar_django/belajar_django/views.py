from django.http import HttpResponse as response
from django.http import HttpRequest as request
from django.shortcuts import render

def index(request):
  return render(request, 'index.html')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Helloooo World")


def resume(request):
    return render(request, 'resume_app/index.html')

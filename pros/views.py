
from django.shortcuts import render, redirect

from django.http import HttpRequest

def index(request):
    return render(request,'index.html')
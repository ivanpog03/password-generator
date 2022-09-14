from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    # use templates from templates folder with render-fucntion

    return render(request, 'generator/home.html')


def password(request):
    return render(request, 'generator/password.html')

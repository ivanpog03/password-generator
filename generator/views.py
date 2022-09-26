import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    # use templates from templates folder with render-fucntion

    return render(request, 'generator/home.html')


def password(request):
    characters = list('ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz1234567890*+%&$=')
    length = 12
    newpassword = ''
    for x in range(length):
        newpassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': newpassword})


def generating(request):
    return render(request, 'generator/generating.html')

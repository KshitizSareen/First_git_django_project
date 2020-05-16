from django.shortcuts import render
from . import machine_learning


def home(request):
    return render(request, 'index.html')


def contact(request):
    name = request.GET['user_input']
    user_input = machine_learning.multiplier(name)
    return render(request, 'contact.html', {'home_input': user_input})

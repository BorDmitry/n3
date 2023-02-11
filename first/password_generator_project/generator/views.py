from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):  # request должен быть всегда
    lst = list(range(6, 18))
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]
    # upchar = [chr(i) for i in range(65, 91)]
    # cifri = [chr(i) for i in range(48, 58)]
    # specsimvol = [chr(i) for i in range(35, 48)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('special'):
        char.extend([chr(i) for i in range(35, 40)])

    length = int(request.GET.get('length'))     # Метода Get, Post нету. Поэтому - это обращение к элементу length
    # uppercase = request.GET.get('uppercase')
    # numbers = request.GET.get('numbers')
    # special = request.GET.get('special')

    psw = ''
    for i in range(length):
        psw += random.choice(char)
    #     if uppercase and numbers and special:
    #         psw += random.choice(char + upchar + cifri + specsimvol)
    #     elif uppercase and numbers:
    #         psw += random.choice(char + upchar + cifri)
    #     elif uppercase and special:
    #         psw += random.choice(char + upchar + specsimvol)
    #     elif numbers and special:
    #         psw += random.choice(char + cifri + specsimvol)
    #     elif uppercase:
    #         psw += random.choice(char + upchar)
    #     elif numbers:
    #         psw += random.choice(char + cifri)
    #     elif special:
    #         psw += random.choice(char + specsimvol)
    #     else:
    return render(request, 'generator/password.html', {'password': psw})


def description(request):
    return render(request, 'generator/description.html')


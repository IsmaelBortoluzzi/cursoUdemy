from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def sobre(request):
    return render(request, 'sobre/sobre.html')


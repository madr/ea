from django.shortcuts import render


def home(request):
    return render(request, "invitation/home.html")

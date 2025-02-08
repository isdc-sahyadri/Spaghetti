from django.shortcuts import render

def index(request):
    return render(request, "l_f/home.html")

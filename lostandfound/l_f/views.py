from django.shortcuts import render

def home(request):
    return render(request, "l_f/home.html")

def find_item(request):
    return render(request, "l_f/find_item.html")

def about_page(request):
    return render(request,"l_f/about_page.html")

def post_item(request):
    return render(request, "l_f/post_item.html")

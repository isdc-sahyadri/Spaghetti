from django.shortcuts import render, redirect,get_object_or_404
from .models import LostItem

def home(request):
    return render(request, "l_f/home.html")

def about_page(request):
    return render(request, "l_f/about_page.html")


def post_lost_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        lost_item = LostItem(
            name=name, 
            email=email, 
            phone=phone, 
            title=title, 
            description=description, 
            image=image
        )
        lost_item.save()

        return redirect('find_item') 

    return render(request, "l_f/post_item.html")

def find_item(request):
    items = LostItem.objects.all().order_by('-created_at')
    return render(request, "l_f/find_item.html", {"items": items})

def delete_item(request, item_id):
    if request.method == "POST":  
        item = get_object_or_404(LostItem, id=item_id)
        item.delete()  
        return redirect('find_item') 

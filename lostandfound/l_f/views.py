from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import SignupForm
from .models import LostItem
from django.contrib.auth.models import User

@login_required(login_url="login")
def home(request):
    return render(request, "l_f/home.html")

def login(request): 
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home")  
        else:
            messages.error(request, "Invalid username or password.") 

    return render(request, "l_f/login.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  
            return redirect("home")  
    else:
        form = SignupForm()

    return render(request, "l_f/sign_up.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def post_lost_item(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        image = request.FILES.get("image")
        status = request.POST.get("status")  

        lost_item = LostItem(
            user=request.user,  
            title=title,
            description=description,
            email=email,
            phone=phone,
            image=image,
            status=status,  
        )
        lost_item.save()

        return redirect("find_item")  

    return render(request, "l_f/post_item.html")

def find_item(request):  
    items = LostItem.objects.all().order_by('-created_at')
    return render(request, "l_f/find_item.html", {"items": items})

@login_required(login_url="login")
def delete_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    
    if request.user == item.user:
        item.delete()
        messages.success(request, "Item deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this item.")

    return redirect("find_item")

def about_page(request):
    return render(request, "l_f/about_page.html")

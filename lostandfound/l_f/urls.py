from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("find/", views.find_item, name="find_item"), 
    path("post/", views.post_lost_item, name="post_item"),
    path("about/", views.about_page, name="about_page"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("find",views.find_item,name="find_item"),
    path("post",views.post_item,name="post_item"),
]
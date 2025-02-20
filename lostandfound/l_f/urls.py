from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("find/", views.find_item, name="find_item"),
    path("post/", views.post_lost_item, name="post_item"),
    path("about/", views.about_page, name="about_page"),
    path("signup/", views.signup, name="signup"),  
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("delete/<int:item_id>/", views.delete_item, name="delete_item"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("home/<param>", views.home, name="home"),    
    path("contactus", views.contactus, name="contactus"),
    path("aboutus", views.aboutus, name="aboutus"),
]
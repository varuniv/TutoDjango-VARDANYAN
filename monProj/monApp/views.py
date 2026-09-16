from django.shortcuts import HttpResponse 

def home(request,param=""):
    return HttpResponse("<h1>Bonjour " + param + " !<h2>")

def contactus(request):
    return HttpResponse("<h1>Contact Us</h1>")

def aboutus(request):
    return HttpResponse("<h1>Something about us</h1>")

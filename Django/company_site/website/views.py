from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{"name":"Crushaders"})

def about(request):
    return render(request,"about.html",{"name":"Crushaders"})

def contact(request):
    return render(request,"contact.html",{"name":"Crushaders"})
from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request,'index.html')

def about(request): 
    return render(request,'aboutus.html')

def contact(request): 
    return render(request,'contactus.html')

def menu(request): 
    return render(request,'menu.html')
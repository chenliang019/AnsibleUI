from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,"views/dashboard.html",status=200)

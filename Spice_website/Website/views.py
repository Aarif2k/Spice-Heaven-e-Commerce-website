from django.shortcuts import render
# from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')
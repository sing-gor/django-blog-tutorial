from django.shortcuts import render
# Create your views here.
def home(request):

    return render(request,'home.html')
def index(request):

    return render(request,'index.html')

def show_1(request):

    return render(request,'show_1.html')

def show_2(request):

    return render(request,'show_2.html')

def show_3(request):

    return render(request,'show_3.html')

def show_4(request):

    return render(request,'show_4.html')
